from django import forms
from .models import Biblioteca

class bibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ('estudiantes_en_articulo','numeral')
        widgets = {}