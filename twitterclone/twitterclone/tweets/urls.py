from twitterclone.tweets import models
from django.contrib import admin
from django.urls import path
from twitterclone.tweets import views



urlpatterns = [
    path('crafttweet/',views.craft_tweet),
    path("tweet/<int:id>/", views.tweet),
    path('', views.feed )
]