from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet

def authorview(request, id):
    html = 'authorview.html'
    twitter_user = TwitterUser.objects.filter(id=id)
    return render(request, html, { 'twitter_user' : twitter_user })
