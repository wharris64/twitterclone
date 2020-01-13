import re
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.tweets.models import Tweet
from twitterclone.tweets.forms import MakeTweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification


@method_decorator(login_required, name='dispatch')
class CraftTweet(View):
    html = "craft_tweet.html"
    form = MakeTweet
    def post(self, request):
        form = MakeTweet(request.POST)
        if form.is_valid():
            data= form.cleaned_data
        tweet = Tweet.objects.create(
            twitteruser=TwitterUser.objects.get(user=request.user),
            description=data['description']
            )
        if "@" in tweet.description:
            target_users = re.findall(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)", tweet.description)
            for i in target_users:
                Notification.objects.create(
                    to=TwitterUser.objects.filter(user__username=i).first(),
                    message=tweet
                    )
            return redirect('/')
    def get(self, request):
        form = MakeTweet()
        return render(request, self.html, {"form": form})
        

# @login_required
# def craft_tweet(request):
#     html = "craft_tweet.html"
#     form = None
#     if request.method == "POST":
#         form = CraftTweet(request.POST)
        

#         if form.is_valid():
#             data= form.cleaned_data
#             Tweet.objects.create(
#                 twitteruser=request.user.twitteruser,
#                 description=data['description']
#             )
#             return redirect('/')
#     else:
#         form = CraftTweet()
#     return render(request, html, {"form": form})


class TweetView(View):
    html = "tweet.html"
    def get(self, request, id):
        tweet = Tweet.objects.filter(id=id)
        return render(request, self.html, {'tweet':tweet})

@method_decorator(login_required, name='dispatch')
class Feed(View):
    html = 'index.html'
    def get(self, request):
        author_tweets = Tweet.objects.filter(twitteruser=request.user.twitteruser)
        following_tweets = Tweet.objects.filter(twitteruser__in=request.user.twitteruser.following.all())
        combined_tweets = author_tweets | following_tweets
        feed = combined_tweets.order_by("-created_at")
        return render(request, self.html, {"data":feed})



# @login_required
# def feed(request):
#     html = "index.html"
#     feed = Tweet.objects.filter().order_by("-created_at")
#     return render(request, html, {"data":feed})