from django.db import models
from twitterclone.twitterusers.models import TwitterUser


class Tweet(models.Model):
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.IntegerField()
    retweets = models.IntegerField()
    