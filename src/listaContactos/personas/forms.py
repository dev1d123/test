from django import forms
from .models import Persona

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder': 'Solo tu nombre porfavor',
                'id': 'nombreID',
                'class': 'special',
                'cols:': '10',
            }
        )

    )
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()