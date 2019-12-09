from django import forms
from twitterclone.tweets.models import Tweet

class CraftTweet(forms.Form):
    description = forms.CharField(max_length=140)