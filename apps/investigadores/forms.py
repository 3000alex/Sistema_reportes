from django import forms
from .models import Modelo14

class informacionAdicionalF(forms.ModelForm):
    """
    telescopio = 
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control mb-1 col-sm-10'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-1 col-sm-10'}),label='Descripción:',)
    file = forms.FileField(widget=forms.TextInput(attrs={'class': 'form-control mb-1 col-sm-10'}))
    """
    class Meta:
        model = Modelo14
        fields = ('TelescopioInstrumentoInfra','url','descripcion','anexos')
        widgets = {
            'TelescopioInstrumentoInfra':forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-1 col-sm-10','id':'telescopioModelo14 {{modelo14.id}}'}))
        }