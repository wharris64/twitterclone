from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    name = models.CharField(max_length = 50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False, blank=True )
    def __str__(self):
            return self.name

