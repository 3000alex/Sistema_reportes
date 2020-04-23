from .settings import *
DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema_reportes',
        'USER': 'FernandoFabian',
        'PASSWORD':'(s(n+k{D#c{}%/[*S0n3',
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE':'America/Mexico_City',
        'OPTIONS': {
            'charset': 'utf8mb4'  # This is the important line
        }
    }
}