from django import forms
from django.contrib.auth.models import User
from twitterclone.twitterclone.twitterusers.models import TwitterUser
from django.contrib.auth.models import User

class EditBio(forms.form):
    bioseftion = forms.Textarea()
    user = forms.CharField(min_length = 5, max_length = 22)
