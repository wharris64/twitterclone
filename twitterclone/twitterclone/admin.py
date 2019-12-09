from django.contrib import admin


from twitterclone.tweets import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
# from twitterclone.notifications import models

admin.site.register(models.Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notification)
