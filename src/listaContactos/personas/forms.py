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

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
        ]
    def clean_nombres(self, *args, **kwargs):
        print('paso')
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra en mayusculas')
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if apellidos.istitle():
            return apellidos
        else:
            raise forms.ValidationError('La primera letra en mayúsculas')

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 0:
            raise forms.ValidationError('La edad no puede ser negativa')
        elif edad > 100:
            raise forms.ValidationError('La edad no puede ser mayor de 100')
        return edad

    def clean_donador(self):
        donador = self.cleaned_data.get('donador')
        if not isinstance(donador, bool):
            raise forms.ValidationError('El campo donador debe ser Verdadero o Falso')
        return donador