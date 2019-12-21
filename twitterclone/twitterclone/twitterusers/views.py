from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from django.contrib.auth.models import User

def authorview(request, id):
    html = 'authorview.html'
    twitter_user = TwitterUser.objects.filter(id=id).first()
    user_tweets = Tweet.objects.filter(twitteruser=twitter_user)
    tweet_count = user_tweets.count()
    user_following = request.user.twitteruser.following.all()
    following_count = user_following.count()
    

    return render(request, html, { 'twitter_user' : twitter_user,"tweet_count":tweet_count, "user_following": user_following, "user_tweets":user_tweets })
@login_required
def profileview(request, id):
    html = 'profileview.html'
    loggedid =  request.user.twitteruser.id
    twitter_user = TwitterUser.objects.filter(id=loggedid).first()
    user_tweets = Tweet.objects.filter(twitteruser=twitter_user)
    tweet_count = user_tweets.count()
    user_following = request.user.twitteruser.following.all()
    following_count = user_following.count()
    return render(request, html, { 'twitter_user' : twitter_user, "tweet_count": tweet_count, "following_count" : following_count, "user_tweets":user_tweets })

def follow_twitter_user(request, id):
    targeted_user = TwitterUser.objects.filter(id=id).first()
    current_user = request.user.twitteruser
    current_user.following.add(targeted_user)
    return redirect(request.META.get('HTTP_REFERER', '/'))
def unfollow_twitter_user(request, id):
    targeted_user = TwitterUser.objects.filter(id=id).first()
    current_user = request.user.twitteruser
    current_user.following.remove(targeted_user)
    return redirect(request.META.get('HTTP_REFERER', '/'))