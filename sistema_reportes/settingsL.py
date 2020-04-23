from .settings import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema_reportes',
        'USER': 'root',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE':'America/Mexico_City',
        
    }
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True