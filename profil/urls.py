from django.conf.urls import url
from profil.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]