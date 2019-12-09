from twitterclone.twitterusers import models
from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views
from twitterclone.authentication import views



urlpatterns = [
    path("createuser/", views.create_user),
    path('login/', views.user_login),
    path('logout/',views.logout_view)
    
    
]