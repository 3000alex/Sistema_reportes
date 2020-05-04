from .settings import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME',"LOCAL"),
        'USER': get_secret('USER',"LOCAL"),
        'PASSWORD':get_secret('PASSWORD',"LOCAL"),
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE':'America/Mexico_City',
    }
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True