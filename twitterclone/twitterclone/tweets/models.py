from django.db import models
from django.utils.timezone import now
from twitterclone.twitterusers.models import TwitterUser

class Tweet(models.Model):
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.IntegerField(blank=True, null=True, default=0)
    retweets = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(default=now, editable=False)

    