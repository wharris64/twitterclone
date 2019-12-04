from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.twitterclone.authentication.forms import CreateUser, LoginUser
from twitterclone.twitterclone.twitterusers.models import TwitterUser

# def profile
def create_user(request):
    html = "create_user.html"
    form = None
    
    if request.method =="POST":
            
        form = CreateUser(request.POST)
            
        if form.is_valid():
            data = form.cleaned_data

            usermake =  User.objects.create(
                username=data['username'],
                password=data['password']
            )
            TwitterUser.objects.create(
                name=data['name'],
                user=usermake
            )
                
        return redirect('/')
    else:
        form = CreateUser()
    
def user_login(request):
    html = "user_login.html"
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
            return redirect(request.GET.get("next", '/'))
    return render(request, html, {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/')
