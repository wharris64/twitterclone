from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet

class Notification(models.Model):
    seen = models.BooleanField(default=False),
    to = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Tweet, on_delete=models.CASCADE)