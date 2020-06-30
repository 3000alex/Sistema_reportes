from apps.reportes.models import Periodo
from datetime import timedelta
import datetime
from django.http import HttpResponse
from django.views.generic import View
from apps.reportes.models import Citas
from apps.registration.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def nuevo_periodo():
    usuarios = User.objects.exclude(is_superuser = 1)
    dateNow = datetime.datetime.now()


    if dateNow.month <= 6:
        nombre_periodo = str(dateNow.year)+"A: "+"ene-jun"

    else: 
        nombre_periodo = str(dateNow.year)+"B: "+"ene-dic"
    
    p = Periodo.objects.create(nombre_periodo=nombre_periodo)
        

    body = render_to_string(
        'administradores/periodoCreado.html', {
            'periodo': p.nombre_periodo,
                
        },
    )
    

    #Envio de correo a todos los reportes con el nuevo periodo.
    for user in usuarios:

        email_message = EmailMessage(
            subject='Nuevo periodo '+p.nombre_periodo+' disponible en la plataforma',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[user.email],
        )
        email_message.content_subtype = 'html'
        email_message.send()