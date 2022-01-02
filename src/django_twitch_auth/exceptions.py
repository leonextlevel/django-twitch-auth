class DjangoTwitchAuthError(Exception):
    def __init__(self):
        super().__init__(
            "You must provide TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET"
            "and TWITCH_REDIRECT_URI to your settings."
        )
