from django.urls import path

from .views import twitch_authorize


urlpatterns = [
    path('authorize/', twitch_authorize, name="django_twitch_auth_authorize"),
]
