from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%gmzr)1n3^6m=0w^0y@^5mewmjb4yn*b#j6#-(f=6uy4)dg&+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# allowed host in VPS
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': '',
        'PORT': 'db_port_number',
    }
}