from django.conf.urls import url
from django.urls import path
from SearchIn.user.views import UserRegistrationView
from SearchIn.user.views import UserLoginView


urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('signin', UserLoginView.as_view()),
]
