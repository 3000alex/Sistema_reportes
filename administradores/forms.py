from django.contrib.auth.forms import UserCreationForm
from registration.models import User
from django import forms

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(required=True, label="Nombre(s) ")
  last_name = forms.CharField(required=True, label="Apellido(s) ")

  class Meta:
    model = User
    fields = ("first_name","last_name","username","password1","password2")
    help_texts = {
       'username':'Requerido. 150 carácteres como máximo.',
     }


class CorreoAlternativo(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("correoAlternativo",)
        widgets = {
        'correoAlternativo': forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba su correo alternativo','disabled':'True'}),
        }
    