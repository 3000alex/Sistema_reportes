from django import forms 

class num61(forms.Form):
    telescopio = forms.CharField(label='Telescopio, instrumento, infraestructura', widget=forms.TextInput(
        attrs={"class":"form-control mb-3",}
    ))

    url = forms.URLField(label="Url", widget = forms.TextInput(
        attrs={"class":"form-control mb-3"}
    ))

    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea(
        attrs={"class":"form-control mb-3", "rows":3}
    ))

    anexo = forms.FileField(label="Anexo")