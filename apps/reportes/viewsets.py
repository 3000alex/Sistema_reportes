from .serializers import Modelo1Serializer
from .models import Modelo1
#rest-framework 
from rest_framework import viewsets


class modelo1Prueba(viewsets.ModelViewSet):
    serializer_class = Modelo1Serializer
    queryset = Modelo1.objects.all()