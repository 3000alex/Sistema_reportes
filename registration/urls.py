from django.contrib import admin
from django.urls import path
from . import views as vista

registrationpatterns = ([
    path('', vista.login_view,name="login"),
    path('perfil/',vista.ProfileUpdate.as_view(), name="actualizar-perfil"),
],'registration')