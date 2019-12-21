from django import forms
from twitterclone.tweets.models import Tweet

class MakeTweet(forms.Form):
    description = forms.CharField(max_length=140)