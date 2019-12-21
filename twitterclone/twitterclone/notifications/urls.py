from django.urls import path
from twitterclone.notifications import views

urlpatterns = [
    path('notifications/', views.NotificationView.as_view())
]
