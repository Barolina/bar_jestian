from .common import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!!')
ALLOWED_HOSTS = ["*"]

for config in TEMPLATES:
    config['OPTIONS']['debug'] = DEBUG

# Mail settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

# debug toolbar

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', 'autofixture',)

