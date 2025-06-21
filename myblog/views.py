from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.models import Post
from .forms import RegistrationForm
from datetime import date
from django.contrib.auth import login

# Create your views here.
def homepage(request):
    # return HttpResponse("Hello Django")
    return render(request, "homepage.html") #To render HTML, use render instead of HttpResponse 

def aboutpage(request):
    return HttpResponse("This is my about page")

def contactuspage(request):
    return HttpResponse("This is our contact us page")

def ourservicespage(request):
    return HttpResponse("This is our services page")

def register_user(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user) # login user automatically
            return redirect("postlist")
    else:
        # for GET request
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})
    
