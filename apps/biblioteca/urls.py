from django.urls import path
from . import views


bibliotecapatterns = ([ 
    #Rutas biblioteca
    path('biblioteca-personal', views.biblioteca_personal.as_view(), name="biblioteca_personal"),
    path('busqueda-biblioteca', views.busqueda_biblioteca.as_view(), name="busqueda_biblioteca"),
    path('editar-biblioteca', views.editar_biblioteca.as_view(), name="editar-biblioteca"),
    path('eliminar-biblioteca', views.eliminar_biblioteca.as_view(), name="eliminar-biblioteca"),
    #Rutas de API ADS
    path('publicaciones-generales', views.publicaciones_generales.as_view(), name="publicaciones_generales"),
    path('publicaciones-bidcode',views.publicaciones_bidcode.as_view(), name="publicaciones_bidcode"),
    path('publicaciones-orcid',views.publicaciones_orcid.as_view(),name="publicaciones_orcid"),
    path('agregar-biblioteca',views.agregar_biblioteca.as_view(), name="agregar-biblioteca"),

],'biblioteca')
