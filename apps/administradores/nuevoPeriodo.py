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
    print('iam an cron job')
    f = open('/home/alexis/Documentos/django_cron.txt', 'w')
    f.close()