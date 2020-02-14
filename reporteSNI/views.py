from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView
# Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from SNIads import SNIads
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
# Create your views here.

@method_decorator(login_required, name='dispatch')
class instruccionesSNI(View):
    def get(self,request):
        return render(request, 'reporteSNI/instrucciones.html')

@method_decorator(login_required, name='dispatch')
class reporteSNI(View):
    def get(self,request):
        return render(request, 'reporteSNI/reporteSNI.html')

@method_decorator(login_required, name='dispatch')
class metodo1ReporteSNI(View):
    def get(self,request):
        author = request.GET.get('autor','None')
        articulos = SNIads.get_papers(author, token=token)
        citas = SNIads.get_citations(articulos, token=token)
        SNIads.print_results(author, articulos, citas)
        f = open(BASE_DIR + '/media/reporteSNI/refs_{}.tex'.format(SNIads.clean_author(author)), 'w+r')
        SNIads.print_results(author,articulos,citas,f)
        response = HttpResponse(f, content_type="text/plain")
        f.close()
        return response

        #SNIads autor -t token

@method_decorator(login_required, name='dispatch')
class metodo2ReporteSNI(View):
    def get(self,request):
        autor = request.GET.get('autor','None')
        print(autor)
        print("Metodo2")
        biblioteca = []


