from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%gmzr)1n3^6m=0w^0y@^5mewmjb4yn*b#j6#-(f=6uy4)dg&+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# allowed host in VPS
ALLOWED_HOSTS = ['*', 'localhost']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

############ DEVUF TOOLBAR ###################
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# Django Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
