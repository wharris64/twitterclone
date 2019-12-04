from twitterclone.twitterclone.tweets import models
from django.contrib import admin
from django.urls import path
from twitterclone.twitterclone.twitterusers import views
admin.site.register(models.Tweets)


urlpatterns = [
    path('crafttweet/',views.craft_tweet),
    path("tweet/<intid>", views.tweet)
]