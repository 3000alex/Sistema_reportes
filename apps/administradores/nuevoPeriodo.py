from apps.investigadores.models import Periodo
from datetime import timedelta
import datetime
from django.http import HttpResponse
from django.views.generic import View
from apps.investigadores.models import Citas
from apps.registration.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def nuevo_periodo(request):
    usuarios = User.objects.exclude(is_superuser = 1)
    dateNow = datetime.datetime.now()
        
    if dateNow.month <= 6:
        nombrePeriodo = str(dateNow.year)+"A: "+"ene-jun"

    else: 
        nombrePeriodo = str(dateNow.year)+"B: "+"ene-dic"
        
    p = Periodo.objects.create(nombrePeriodo=nombrePeriodo)
        
    for user in usuarios:
            
        Citas.objects.create(
            numeral_id = 31, periodo_id = p.id, usuario_id = user.id
        )

    body = render_to_string(
        'administradores/periodoCreado.html', {
            'periodo': p.nombrePeriodo,
                
        },
    )

    #Envio de correo a todos los investigadores con el nuevo periodo.
    for user in usuarios:

        email_message = EmailMessage(
            subject='Nuevo periodo '+p.nombrePeriodo+' disponible en la plataforma',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[user.email],
        )
        email_message.content_subtype = 'html'
        email_message.send()