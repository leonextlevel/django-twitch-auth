import requests

from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect
from django.urls.base import reverse

from .settings import (
    TWITCH_CLIENT_ID,
    TWITCH_CLIENT_SECRET,
    TWITCH_REDIRECT_URI,
    TWITCH_TOKEN_URL,
    TWITCH_AUTHORIZE_URL,
    TWITCH_REDIRECT_URI,
)

class TwitchLoginMixin:

    def _generate_token(self, request):
        code = request.GET.get('code', None)
        if code is not None:
            token_params = {
                'client_id': TWITCH_CLIENT_ID,
                'client_secret': TWITCH_CLIENT_SECRET,
                'code': code,
                'redirect_uri': TWITCH_REDIRECT_URI,
                'grant_type': 'authorization_code',
            }
            response = requests.post(TWITCH_TOKEN_URL, params=token_params)
            if response.ok:
                credentials = response.json()
                request.session['refresh_token'] = credentials['refresh_token']
                request.session['access_token'] = credentials['access_token']
                return request.session['access_token']
        return None

    def _get_token(self, request):
        try:
            return request.session['access_token']
        except KeyError:
            return self._generate_token(request)

    def get(self, request, *args, **kwargs):
        redirect_url = request.GET.get('next') or reverse(settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated:
            return redirect(redirect_url)
        token = self._get_token(request)
        if token is not None:
            user = auth.authenticate(request, token=token)
            auth.login(request, user)
            return redirect(redirect_url)
        return super().get(request, *args, **kwargs)


def twitch_authorize(request):
    url = (
        f'{TWITCH_AUTHORIZE_URL}?'
        f'client_id={TWITCH_CLIENT_ID}&'
        f'redirect_uri={TWITCH_REDIRECT_URI}&'
        'response_type=code&'
        'scope=channel_read'
    )
    return redirect(url)
