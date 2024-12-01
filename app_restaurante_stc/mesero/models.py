

from django.db import models

# Create your models here.
class Mesero(models.Model):
    nombre = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20,default='')
    edad = models.IntegerField(default=0)
    dni = models.CharField(max_length=8,default='00000000')