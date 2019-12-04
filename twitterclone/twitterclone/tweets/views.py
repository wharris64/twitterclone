from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.twitterclone.tweets.models import Tweets
from twitterclone.twitterclone.tweets.forms import CraftTweet

@login_required
def craft_tweet(request):
    html = "craft_tweet.html"
    form = None
    if request.method == "POST":
        form = CraftTweet(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            Tweets.objects.create(
                
                description=data['description'],
            )
            return render(request, "thanks.html")
    else:
        form = CraftTweet()
    return render(request, html, {"form": form})

def tweet(request, id):
    html = "tweet.html"
    tweet = Tweets.objects.filter(id=id)
    return render(request, html, {'tweet':tweet})