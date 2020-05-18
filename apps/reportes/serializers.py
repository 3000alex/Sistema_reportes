from rest_framework import serializers
from .models import Modelo1

class Modelo1Serializer(serializers.ModelSerializer):
    class Meta:
        model= Modelo1
        fields= "__all__"

