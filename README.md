<h1>Django Chatbot (OpenAI API)</h1>

<h3>Description:</h3> 

Welcome to the simple django chabot integrated with openai API. This app is using chat gpt 3-5 turbo (tried to implement gpt 4, but it needs at least one purchase which i do not have on my acc). 
 ---

<h3>Table of Contents:</h3> 

 

Installation 

Features 

Usage 

Configuration 

Security 

Contributing 

License 


 

 

 ---

<h3>Installation:</h3> 

 

To run gym management system, follow these steps: 

 

Clone the repository on your machine: 

 
	git clone https://github.com/pavle0402/Django-E-Learning-System.git

 

Navigate to the project directory: 

cd your-path-to-chatbot 

 

3. Create a virtual environment (optional but recommended) and activate it: 

python –m venv venv 

 

 

4. Activate your virtual environment: 

On windows: 

venv/Scripts/activate 

 

On macOS/Linux: 

Source venv/bin/activate 

 

5. Install project dependencies: 
	pip install –r requirements.txt (there are many packages in this requirements, since this was my virtual environment I use for most of the project. I think you need just a few to run this project, but it will not hurt to install all of these. 

 

6. Configure database connections in settings.py. 

 

7. Apply database migrations: 

py manage.py migrate 

 

8. Create superuser(staff) account: 

py manage.py createsuperuser(then you will be asked to provide 	username, email and password) - creating staff user

Or just register as a regular user through the app. This is easier.

9. Start a development server: 

py manage.py runserver 

 

Application should now be running on: http://localhost:8000. 

 

 
---
<h3>Key Features:</h3> 

- **User Authentication:** Users can register, log in, and log out securely.
- **Homepage:** Explore frequently asked questions (FAQs), top-rated courses, and an app overview.
- **Instructor Profiles:** Discover instructors, their skills, and the courses they teach.
- **Course Listings:** View a list of available courses.
- **Course Details:** Access detailed information about each course, including descriptions, prices, and user ratings.
- **Enrollment:** Users can enroll in courses to access the course content.
- **User Profiles:** Personalized user profiles display profile pictures, social media links, and the courses they have enrolled to.
- **Feedback Section:** Share feedback and ratings for each course.
 

 
 ---

<h3>Screenshots:</h3> 

Chatbot:

<img src="chatbot_screenshots/chat2.png" width=450 height=350>

Authentication:

<img src="chatbot_screenshots/login.png" width=450 height=350>
<img src="chatbot_screenshots/register.png" width=450 height=350>


 As there are many screenshots for this project, i won't attach them here. You can check all the other pictures in "chatbot_screenshots/" folder inside this repository.
 There you can find all the functionalities, like deleting chat history which i think is really important, logout and many more...
 ---

<h3>Technologies used</h3> 

- Frontend: HTML, CSS, JavaScript
- Backend: Django
- Database: SQLite(django's default)
- Other third-party packages and libraries
 

  ---


<h3>Contributing</h3> 

Contributions to the project are welcome! If you would like to contribute, please follow these guidelines: 

Fork the repository. 

Create a new branch for your feature or bug fix. 

Make your changes and commit them with descriptive messages. 

Push your branch to your fork. 

Submit a pull request with a clear explanation of your changes. 

 
 ---

<h3>Creating process:</h3> 
<p1 style="text-align:center;">
	
**Project Overview**

Welcome to chatbot. This is like a clone of ChatGPT. I created this just to practice working with open APIs, I think can be really useful. Frontend on this app is not really advanced, there are some nice functionalities like some buttons, but i didn't spend 
much time working on frontend since that was not the goal of this project, and also I didn't have much time since I am working on other projects as well (Fast API). This was just a nice addition to my portfolio. 
There are functionalities like saving chat history, deleting chat history, user authentication, home page with FAQ and login and register buttons, some small details like arrow that puts user back to top of chat and so on... 
Hope you like it! :)

 </p1>

For any questions or inquiries, contact me at pavles2002@gmail.com 

