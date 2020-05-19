from .settings import *
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistema_reportes',
        'USER': 'postgres',
        'PASSWORD':'0442223196995a',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True