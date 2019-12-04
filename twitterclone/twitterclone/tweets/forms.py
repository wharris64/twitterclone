from django import forms
from twitterclone.twitterclone.tweets.models import Tweets

class CraftTweet(forms.Form):
    description = forms.CharField(max_length=140)