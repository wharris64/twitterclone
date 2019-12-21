from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.tweets.models import Tweet
from twitterclone.tweets.forms import MakeTweet
from twitterclone.twitterusers.models import TwitterUser


@method_decorator(login_required, name='dispatch')
class CraftTweet(View):
    html = "craft_tweet.html"
    form = MakeTweet
    def post(self, request):
        if request.method == "POST":
            form = MakeTweet(request.POST)
            if form.is_valid():
                data= form.cleaned_data
            Tweet.objects.create(
                twitteruser=TwitterUser.objects.get(user=request.user),
                description=data['description']
            )
            return redirect('/')
    def get(self, request):
        form = MakeTweet()
        return render(request, self.html, {"form": form})
        

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

# def tweet(request, id):
#     html = "tweet.html"
#     tweet = Tweet.objects.filter(id=id)
#     return render(request, html, {'tweet':tweet})
class TweetView(View):
    html = "tweet.html"
    def get(self, request, id):
        tweet = Tweet.objects.filter(id=id)
        return render(request, self.html, {'tweet':tweet})

@method_decorator(login_required, name='dispatch')
class Feed(View):
    html = 'index.html'
    def get(self, request):
        feed = Tweet.objects.filter().order_by("-created_at")
        return render(request, self.html, {"data":feed})



# @login_required
# def feed(request):
#     html = "index.html"
#     feed = Tweet.objects.filter().order_by("-created_at")
#     return render(request, html, {"data":feed})