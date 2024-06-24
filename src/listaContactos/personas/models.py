from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()#(max_digits=3)
    donador = models.BooleanField(blank=False) 
    def get_absolute_url(self):
        return "/personas/" + str(self.id) + "/"