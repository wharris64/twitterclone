from django import forms
from django.contrib.auth.models import User
from twitterclone.twitterclone.twitterusers.models import TwitterUser
from django.contrib.auth.models import User
class CreateUser(forms.Form):
    user = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)

class LoginUser(forms.Form):
    user = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)