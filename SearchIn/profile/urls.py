from django.conf.urls import url
from django.urls import path
from SearchIn.profile.views import UserProfileView


urlpatterns = [
    path('profile', UserProfileView.as_view()),
]
