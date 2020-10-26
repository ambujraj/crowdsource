from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "home.html", {})
    else:
        return render(request, "home_other.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def signup_view(request, *args, **kwargs):
    return render(request, "signup.html", {})

def getfund_view(request, *args, **kwargs):
    return render(request, "getfund.html", {})