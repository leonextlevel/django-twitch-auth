import requests

from django.conf import settings

from .exceptions import DjangoTwitchAuthError
from .settings import TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET, TWITCH_TOKEN_VALIDATE, TWITCH_TOKEN_URL


class TwitchAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_id = TWITCH_CLIENT_ID
        client_secret = TWITCH_CLIENT_SECRET
        if client_id is None or client_secret is None:
            raise DjangoTwitchAuthError
        try:
            token = request.session['access_token']
            validate_response = requests.get(TWITCH_TOKEN_VALIDATE, headers={
                'Authorization': f'Bearer {token}'
            })
            if validate_response.status_code != 200:
                refresh_token = request.session['refresh_token']
                token_params = {
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'refresh_token': refresh_token,
                    'grant_type': 'refresh_token',
                }
                revalidate_response = requests.post(
                    TWITCH_TOKEN_URL, params=token_params
                )
                if revalidate_response.status_code != 200:
                    request.session.flush()
        except KeyError:
            request.session.flush()

        response = self.get_response(request)

        return response
