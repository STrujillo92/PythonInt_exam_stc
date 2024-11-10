from django.db import models

# Create your models here.
class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)