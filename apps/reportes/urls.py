from django.urls import path
from . import views as vista #apoyo_institucional,desarrollo_tec_inovacion,formacion_RH,home,informacion_adicional,investigacion_cientifica,perfil


reportespatterns = ([
    #Secciones
    path('reporte-productividad',vista.reporte_productividad.as_view(), name='reporte-productividad'),
    path('Ampliar-sesion',vista.ampliarSesion.as_view(), name="Ampliar-sesion"),
    path('apoyo-institucional', vista.apoyo_institucional.as_view(), name="apoyo_institucional"),
    path('desarrollo-tec-inovacion', vista.desarrollo_tec_inovacion.as_view(), name="DTI"),
    path('formacion-RH', vista.formacion_RH.as_view(), name="formacion_RH"),
    path('informacion-adicional', vista.informacion_adicional.as_view(), name="informacion_adicional"),
    path('home', vista.home.as_view(), name="home"),
    path('investigacion-cientifica', vista.investigacion_cientifica.as_view(), name="investigacion_cientifica"),
    #Operaciones de las secciones  
    path('actualizar-Biblioteca',vista.actualizarBiblioteca.as_view(), name="actualizar-Biblioteca"),
    
    #reporte de productividad
    path('generarReporte',vista.generarReporte.as_view(), name="generarReporte"),
    path('reportesEnviados', vista.reportesEnviados.as_view(), name="reportesEnviados"),
    path('descargarReportesEnviado',vista.descargarReporteEnviado.as_view(), name="descargarReporte"),
    #Biblioteca añadir Q1,Q2,Q3,Q4
    path('BibliotecaCrearNumeral',vista.BibliotecaCrearNumeral.as_view(), name="BibliotecaCrearNumeral"),
    path('info-anteriorBiblioteca',vista.infoAnteriorBiblioteca.as_view(), name="info-anteriorBiblioteca"),
    #Investigacion cientifica
    path('actualizar-modelo1',vista.actualizarModelo1.as_view(), name="actualizar-modelo1"),
    path('eliminar-modelo1',vista.eliminarModelo1.as_view(), name="eliminar-modelo1"),
    path('crear-modelo1',vista.crearModelo1.as_view(), name="crear-modelo1"),
    path('info-anteriorModelo1',vista.infoAnteriorModelo1.as_view(), name="info-anteriorModelo1"),
    
    path('actualizar-modelo2',vista.actualizarModelo2.as_view(), name="actualizar-modelo2"),
    path('eliminar-modelo2',vista.eliminarModelo2.as_view(), name="eliminar-modelo2"),
    path('crear-modelo2',vista.crearModelo2.as_view(), name="crear-modelo2"),
    path('info-anteriorModelo2',vista.infoAnteriorModelo2.as_view(), name="info-anteriorModelo2"),

    path('actualizar-modelo3',vista.actualizarModelo3.as_view(), name="actualizar-modelo3"),
    path('eliminar-modelo3',vista.eliminarModelo3.as_view(), name="eliminar-modelo3"),
    path('crear-modelo3', vista.crearModelo3.as_view(), name="crear-modelo3"),
    path('info-anteriorModelo3',vista.infoAnteriorModelo3.as_view(), name="info-anteriorModelo3"),

    #Citas
    path('actualizar-citas',vista.actualizarCitas.as_view(), name="actualizar_citas"),
    path('crear-citas', vista.crearCitas.as_view(), name="crear-citas"),
    #Formacion RRHH - CRUD

    path('actualizar-modelo4',vista.actualizarModelo4.as_view(), name="actualizar-modelo4"),
    path('eliminar-modelo4',vista.eliminarModelo4.as_view(), name="eliminar-modelo4"),
    path('crear-modelo4',vista.crearModelo4.as_view(), name="crear-modelo4"),
    path('info-anteriorModelo4',vista.infoAnteriorModelo4.as_view(), name="info-anteriorModelo4"),

    path('actualizar-modelo5',vista.actualizarModelo5.as_view(), name="actualizar-modelo5"),
    path('eliminar-modelo5',vista.eliminarModelo5.as_view(), name="eliminar-modelo5"),
    path('crear-modelo5',vista.crearModelo5.as_view(), name="crear-modelo5"),
    path('info-anteriorModelo5',vista.infoAnteriorModelo5.as_view(), name="info-anteriorModelo5"),

    path('actualizar-modelo6',vista.actualizarModelo6.as_view(), name="actualizar-modelo6"),
    path('eliminar-modelo6',vista.eliminarModelo6.as_view(), name="eliminar-modelo6"),
    path('crear-modelo6',vista.crearModelo6.as_view(), name="crear-modelo6"),
    path('info-anteriorModelo6',vista.infoAnteriorModelo6.as_view(), name="info-anteriorModelo6"),

    path('actualizar-modelo7',vista.actualizarModelo7.as_view(), name="actualizar-modelo7"),
    path('eliminar-modelo7',vista.eliminarModelo7.as_view(), name="eliminar-modelo7"),
    path('crear-modelo7',vista.crearModelo7.as_view(), name="crear-modelo7"),
    path('info-anteriorModelo7',vista.infoAnteriorModelo7.as_view(), name="info-anteriorModelo7"),

    path('actualizar-modelo8',vista.actualizarModelo8.as_view(), name="actualizar-modelo8"),
    path('eliminar-modelo8',vista.eliminarModelo8.as_view(), name="eliminar-modelo8"),
    path('crear-modelo8',vista.crearModelo8.as_view(), name="crear-modelo8"),
    path('info-anteriorModelo8',vista.infoAnteriorModelo8.as_view(), name="info-anteriorModelo8"),

    path('actualizar-modelo9',vista.actualizarModelo9.as_view(), name="actualizar-modelo9"),
    path('eliminar-modelo9',vista.eliminarModelo9.as_view(), name="eliminar-modelo9"),
    path('crear-modelo9',vista.crearModelo9.as_view(), name="crear-modelo9"),
    path('info-anteriorModelo9',vista.infoAnteriorModelo9.as_view(), name="info-anteriorModelo9"),

    path('actualizar-modelo10',vista.actualizarModelo10.as_view(), name="actualizar-modelo10"),
    path('eliminar-modelo10',vista.eliminarModelo10.as_view(), name="eliminar-modelo10"),
    path('crear-modelo10',vista.crearModelo10.as_view(), name="crear-modelo10"),
    path('info-anteriorModelo10',vista.infoAnteriorModelo10.as_view(), name="info-anteriorModelo10"),

    path('actualizar-modelo11',vista.actualizarModelo11.as_view(), name="actualizar-modelo11"),
    path('eliminar-modelo11',vista.eliminarModelo11.as_view(), name="eliminar-modelo11"),
    path('crear-modelo11',vista.crearModelo11.as_view(), name="crear-modelo11"),
    path('info-anteriorModelo11',vista.infoAnteriorModelo11.as_view(), name="info-anteriorModelo11"),

    path('actualizar-modelo12',vista.actualizarModelo12.as_view(), name="actualizar-modelo12"),
    path('eliminar-modelo12',vista.eliminarModelo12.as_view(), name="eliminar-modelo12"),
    path('crear-modelo12',vista.crearModelo12.as_view(), name="crear-modelo12"),
    path('info-anteriorModelo12',vista.infoAnteriorModelo12.as_view(), name="info-anteriorModelo12"),

    path('actualizar-modelo13',vista.actualizarModelo13.as_view(), name="actualizar-modelo13"),
    path('eliminar-modelo13',vista.eliminarModelo13.as_view(), name="eliminar-modelo13"),
    path('crear-modelo13',vista.crearModelo13.as_view(), name="crear-modelo13"),
    path('info-anteriorModelo13',vista.infoAnteriorModelo13.as_view(), name="info-anteriorModelo13"),

    path('actualizar-modelo14/',vista.actualizarModelo14.as_view(), name="actualizar-modelo14"),
    path('eliminar-modelo14',vista.eliminarModelo14.as_view(), name="eliminar-modelo14"),
    path('crear-modelo14',vista.crearModelo14.as_view(), name="crear-modelo14"),
    path('info-anteriorModelo14',vista.infoAnteriorModelo14.as_view(), name="info-anteriorModelo14"),
    
    path('actualizar-modelo15',vista.actualizarModelo15.as_view(), name="actualizar-modelo15"),
    path('eliminar-modelo15',vista.eliminarModelo15.as_view(), name="eliminar-modelo15"),
    path('crear-modelo15',vista.crearModelo15.as_view(), name="crear-modelo15"),
    path('info-anteriorModelo15',vista.infoAnteriorModelo15.as_view(), name="info-anteriorModelo15"),
    
    path('actualizar-modelo16',vista.actualizarModelo16.as_view(), name="actualizar-modelo16"),
    path('eliminar-modelo16',vista.eliminarModelo16.as_view(), name="eliminar-modelo16"),
    path('crear-modelo16',vista.crearModelo16.as_view(), name="crear-modelo16"),
    path('info-anteriorModelo16',vista.infoAnteriorModelo16.as_view(), name="info-anteriorModelo16"),

    path('prueba/<pk>',vista.infoUpdateView.as_view(), name="prueba"),
    
    #Finalizar reporte
    path('enviar-Reporte',vista.enviarReporte.as_view(), name="enviar-Reporte")
    
],'reportes')
