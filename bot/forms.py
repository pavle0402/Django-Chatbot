from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

genders = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your first name."}))
    last_name = forms.CharField(required=True, max_length= 155, widget=forms.TextInput(attrs={"class":"form-control-sm",
                                                                                "placeholder":"Enter your last name."}))
    username = forms.CharField(required=True, max_length= 155, widget=forms.EmailInput(attrs={"class":"form-control-sm",
                                                                           "placeholder":"Enter your email(username)."}))
    password1 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Enter your password."}))
    password2 = forms.CharField(required=True, max_length=155, widget=forms.PasswordInput(attrs={"class":"form-control-sm",
                                                                            "placeholder":"Confirm your password."}))
    gender = forms.CharField(required=True, widget=forms.Select(choices=genders, attrs={"class":"form-control-sm"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password1', 'password2', 'gender') 