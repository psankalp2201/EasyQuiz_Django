"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from EasyQuiz.views import *

urlpatterns = [
    path('home',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('quiz',quiz,name='quiz'),
    path('signup_admin',signup_admin,name='signup_admin'),
    path('signup_user',signup_user,name='signup_user'),
    path('login_admin',login_admin,name='login_admin'),
    path('login_user',login_user,name='login_user'),
    path('profile_admin',profile_admin,name='profile_admin'),
    path('quiz',quiz,name='quiz'),
    path('sample',sample,name='sample'),
    path('create_quiz',create_quiz,name='create_quiz'),
    path('profile_admin',profile_admin,name='create_quiz'),
    path('profile_user',profile_user,name='profile_user'),
    path('update_quiz',update_quiz,name='update_quiz'),
    path('view_all_quiz',view_all_quiz,name='view_all_quiz'),
    path('start_quiz',start_quiz,name='start_quiz'),

    #Render URL Above#

    
    path('signupAdmin',signupAdmin,name='signupAdmin'),
    path('loginAdmin',loginAdmin,name='loginAdmin'),
    path('signupUser',signupUser,name='signupUser'),
    path('loginUser',loginUser,name='loginUser'),
    path('updateQuiz',updateQuiz,name="updateQuiz"),
    path('deleteQuiz',deleteQuiz,name="deleteQuiz"),
    path('createQuiz',createQuiz,name="createQuiz"),
    path('viewQues',viewQues,name='viewQues'),
    path('addQues',addQues,name='addQues'),
    path('start_qid',start_qid,name='start_qid'),
    path('logout_A',logout_A,name='logout_admin'),
    path('logout_U',logout_U,name='logout_user'),


    
]