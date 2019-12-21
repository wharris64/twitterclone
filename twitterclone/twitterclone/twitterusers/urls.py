from twitterclone.twitterusers import models
from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views



urlpatterns = [
path('authorview/<int:id>/', views.authorview),
path('profileview/<int:id>/', views.profileview),
path('follow_twitter_user/<int:id>/', views.follow_twitter_user ),
path('unfollow_twitter_user/<int:id>/', views.unfollow_twitter_user )

]