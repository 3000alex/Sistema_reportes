from django import forms
from .models import Biblioteca

class bibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ('estudiantesEnArticulo','numeral')
        widgets = {}