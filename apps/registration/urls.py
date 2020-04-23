from django.contrib import admin
from django.urls import path
from . import views 

registrationpatterns = ([
    path('', views.login_view,name="login"),
    path('perfil',views.ProfileUpdate.as_view(), name="actualizar-perfil"),
],'registration')