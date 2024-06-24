from django import forms
from .models import Persona

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(label='Your Name')
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 20)
    donador = forms.BooleanField()