from .settings import *
DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME','PRODUCCION'),
        'USER': get_secret('USER','PRODUCCION'),
        'PASSWORD':get_secret('PASSWORD','PRODUCCION'),
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE':'America/Mexico_City',
        'OPTIONS': {
            'charset': 'utf8mb4'  # This is the important line
        }
    }
}