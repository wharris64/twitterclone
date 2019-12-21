from twitterclone.tweets import models
from django.contrib import admin
from django.urls import path
from twitterclone.tweets import views



urlpatterns = [
    path('crafttweet/',views.CraftTweet.as_view()),
    path("tweet/<int:id>/", views.TweetView.as_view()),
    path('', views.Feed.as_view())
]