from django.conf import settings

TWITCH_AUTHORIZE_URL = getattr(settings, 'TWITCH_AUTHORIZE_URL', 'https://id.twitch.tv/oauth2/authorize')
TWITCH_TOKEN_URL = getattr(settings, 'TWITCH_TOKEN_URL', 'https://id.twitch.tv/oauth2/token')
TWITCH_TOKEN_VALIDATE = getattr(settings, 'TWITCH_TOKEN_VALIDATE', 'https://id.twitch.tv/oauth2/validate')
TWITCH_USERS_URL = getattr(settings, 'TWITCH_USERS_URL', 'https://api.twitch.tv/helix/users')

TWITCH_CLIENT_ID = getattr(settings, 'TWITCH_CLIENT_ID', None)
TWITCH_CLIENT_SECRET = getattr(settings, 'TWITCH_CLIENT_SECRET', None)
TWITCH_REDIRECT_URI = getattr(settings, 'TWITCH_REDIRECT_URI', None)
TWITCH_USERNAME_FIELD = getattr(settings, 'TWITCH_USERNAME_FIELD', 'username')
TWITCH_EMAIL_FIELD = getattr(settings, 'TWITCH_EMAIL_FIELD', 'email')
