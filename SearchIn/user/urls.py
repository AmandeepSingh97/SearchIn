from django.conf.urls import url
from django.urls import path
from SearchIn.user.views import UserRegistrationView


urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
]
