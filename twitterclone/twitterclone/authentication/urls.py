from twitterclone.twitterclone.twitterusers import models
from django.contrib import admin
from django.urls import path
from twitterclone.twitterclone.twitterusers import views



urlpatterns = [
    path("createuser/", views.create_user),
    path('login/', views.login_user)
    
    
]