from twitterclone.twitterusers import models
from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views



urlpatterns = [
path('authorview/<int:id>/', views.authorview),
]