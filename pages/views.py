from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django import forms
# Create your views here.
def home_view(request, *args, **kwargs):
    if(request.user.is_authenticated):
        return render(request, "home.html", {})
    else:
        return render(request, "login.html", {})
    #check for auth to refer to login
def login_view(request, *args, **kwargs):
    if(request.method=='POST'):
        loginemail = request.POST['email']
        loginpassword = request.POST['password']
        user = authenticate(username=loginemail, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, please try again!")
            return redirect("login")
    else:
        return render(request, "login.html", {})

def signup_view(request, *args, **kwargs):
    if(request.method=='POST'):
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username = request.POST['email']).exists():
            messages.error(request, "Email already exists!")
            return redirect("signup")
        else:
            user = User.objects.create_user(password=password, username=email)
            user.save()
            return redirect("login")
    else:
        return render(request, "signup.html", {})

def getfund_view(request, *args, **kwargs):
    if(request.user.is_authenticated):
        return render(request, "getfund.html", {})
        
    else:
        return render(request, "login.html", {})