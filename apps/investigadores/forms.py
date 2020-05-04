from django import forms
from .models import Modelo14


class informacionAdicionalF(forms.ModelForm):
    class Meta:
        model = Modelo14
        fields = ('TelescopioInstrumentoInfra','url','descripcion','anexos')
        widgets = {
            'TelescopioInstrumentoInfra':forms.Select(attrs={'class': 'form-control mb-4'}),
            'url':forms.URLInput(attrs={'class': 'form-control mb-4'}),
            'descripcion':forms.Textarea(attrs={'class': 'form-control mb-4','rows':3, 'cols':15}),
            'anexo':forms.FileInput(attrs={'class': 'form-control'})
        }