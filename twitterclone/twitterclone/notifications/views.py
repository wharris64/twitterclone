from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from twitterclone.notifications.models import Notification


class NotificationView(View):
    html = 'notifications.html'
    def get(self, request):
        current_user = request.user.twitteruser
        notifications = Notification.objects.filter(to=current_user)
        return render(request, self.html, {'notifications':notifications})

