from .base import *
from os import environ as os_environ

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os_environ.get('SECRET_KEY', 'django-insecure-%gmzr)1n3^6m=0w^0y@^5mewmjb4yn*b#j6#-(f=6uy4)dg&+r')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os_environ.get('DEBUG', False,)

ALLOWED_HOSTS = os_environ.get('ALLOWED_HOSTS').split(' ')

# Database DOCKER
DATABASES = {
    'default': {
        'ENGINE': os_environ.get('POSTGRES_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os_environ.get('POSTGRES_DB', str(BASE_DIR / "db.sqlite3"),),
        'USER': os_environ.get('POSTGRES_USER', 'user'),
        'PASSWORD': os_environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST': os_environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os_environ.get('POSTGRES_PORT', '5432'),
    }
}