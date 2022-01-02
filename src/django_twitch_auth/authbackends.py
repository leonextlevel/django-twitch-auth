import requests

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings

from .settings import TWITCH_USERS_URL, TWITCH_CLIENT_ID, TWITCH_USERNAME_FIELD, TWITCH_EMAIL_FIELD


User = get_user_model()


class TwitchBackend(BaseBackend):
    def authenticate(self, request, token=None):
        response = requests.get(
            TWITCH_USERS_URL,
            headers={
                'Accept': 'application/vnd.twitchtv.v5+json',
                'Client-ID': TWITCH_CLIENT_ID,
                'Authorization': f'Bearer {token}',
            }
        )
        if response.ok:
            user_informations = response.json()['data'][0]
            user_data = {
                TWITCH_USERNAME_FIELD: user_informations['login'],
            }
            if TWITCH_EMAIL_FIELD is not None:
                user_data[TWITCH_EMAIL_FIELD] = user_informations['email']
            try:
                user = User.objects.get(**user_data)
            except User.DoesNotExist:
                user = User.objects.create(**user_data)
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
