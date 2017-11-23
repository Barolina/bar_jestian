from .common import *

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['example.com'])
SECRET_KEY = env('DJANGO_SECRET_KEY')
DATABASES['default'] = env.db('DATABASE_URL')
