# Django Twitch Auth

## Dependencies

Install requests if not installed

```bash
pip install requests
```

## Installation

1. Install using pip

```bash
pip install django_twitch_auth
```

2. Add 'django_twitch_auth' to your INSTALLED_APPS setting.

```python
INSTALLED_APPS = [
    ...
    'django_twitch_auth',
]
```

3. Add 'django_twitch_auth.middlewares.TwitchAuthenticationMiddleware' under 'django.contrib.sessions.middleware.SessionMiddleware' to your MIDDLEWARE setting.

```python
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_twitch_auth.middlewares.TwitchAuthenticationMiddleware',
    ...
]
```

4. Add AUTHENTICATION_BACKENDS to your settings.

```python
AUTHENTICATION_BACKENDS = [
    'django_twitch_auth.authbackends.TwitchBackend',
]
```

5. Add the following to your root urls.py file.

```python
urlpatterns = [
    ...
    path('django_twitch_auth/', include('django_twitch_auth.urls'))
]
```

6. Add twitch credentials and redirect uri to your settings

```python
TWITCH_CLIENT_ID = 'client_id_here'
TWITCH_CLIENT_SECRET = 'client_secret_here'
TWITCH_REDIRECT_URI = 'https://redirect_uri_here'
```
