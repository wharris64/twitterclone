from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.tweets.models import Tweet
from twitterclone.tweets.forms import CraftTweet
from twitterclone.twitterusers.models import TwitterUser

@login_required
def craft_tweet(request):
    html = "craft_tweet.html"
    form = None
    if request.method == "POST":
        form = CraftTweet(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            Tweet.objects.create(
                twitteruser=request.user.twitteruser,
                description=data['description']
            )
            return redirect('/')
    else:
        form = CraftTweet()
    return render(request, html, {"form": form})

def tweet(request, id):
    html = "tweet.html"
    tweet = Tweet.objects.filter(id=id)
    return render(request, html, {'tweet':tweet})
@login_required
def feed(request):
    html = "index.html"
    feed = Tweet.objects.filter().order_by("-created_at")
    return render(request, html, {"data":feed})
