from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Chat
from django.utils import timezone
from django.views.generic import DeleteView
from datetime import datetime

API_KEY = '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'
openai.api_key = API_KEY


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"You are a wonderful and inteligent assistant."},
            {"role":"user", "content":message},
        ]

    )
    print(response)
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    chats = Chat.objects.filter(user=request.user.id)
    if request.method == "POST":
        message = request.POST.get('message') #getting message from fetch's body param
        response = ask_openai(message)
        Chat.objects.create(user=request.user, message=message, response=response, created_at=timezone.now())
        # chat_history.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats':chats,})
 
def DeleteChatView(request):
    chat_history = Chat.objects.all().filter(user=request.user)
    if request.method == "POST":
        if chat_history:
            chat_history.delete()
            return JsonResponse({"message":"Chat history successfully deleted."})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('chatbot')
        else:
            messages.warning(request, "Incorrect login information. Try again.")
            return redirect('login')
    return render(request, 'login.html', {})

def register_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chatbot')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')