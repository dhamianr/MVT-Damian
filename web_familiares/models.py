import datetime
from statistics import mode
from django.db import models

# Create your models here.
class Familiares(models.Model):

    nombres = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateField()

