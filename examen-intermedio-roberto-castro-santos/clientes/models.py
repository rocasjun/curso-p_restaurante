from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, default='')
    DNI = models.IntegerField(default=0000000)