from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def users_list(request):
    users = User.objects.all()
    return render(request, "users/users_list.html", {"users":users} )

def usershome(request):
    return render(request, "users/users.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:posts_list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOGIN HERE
            login(request, form.get_user())
            return redirect("posts:posts_list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form":form})