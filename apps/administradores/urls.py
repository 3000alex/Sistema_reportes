from django.urls import path
from . import views
from . import nuevoPeriodo as n


administradorespatterns = ([ 
    path('home-adm', views.home_adm.as_view(), name="home-adm"),
    #Muestra usuarios: 
    path('investigadores', views.UsuariosListado.as_view(), name="reportes"),
    #Edita usuarios
    path('reportes/editar',views.UsuariosEditar.as_view(), name="editar-adm"),
    #Elimina usuarios
    path('reportes/eliminar', views.UsuariosEliminar.as_view(), name='eliminar'),
    #Agregar Usuario
    path('reportes/agregar', views.UsuarioAgregar.as_view(), name="agregar-inv"),
    path('perfil_adm',views.perfil_adm.as_view(), name="perfil_adm"),
    #Reportes
    path('reportes-adm',views.reportes_adm.as_view(), name="reportes_adm"),
    path('reporteMaestro', views.reporteMaestro.as_view(), name="reporteMaestro"),
    #Enviar correo 
    path('correoBienvenida',views.correoBienvenida.as_view(), name="correoBienvenida"),
    #Nuevo periodo
    path('periodoNuevo', n.nuevo_periodo, name='nuevo_periodo'),
    path('tabla-reportes',views.tabla_reportes.as_view(), name="tabla_reportes")

],'administradores')