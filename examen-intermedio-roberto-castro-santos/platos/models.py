from django.db import models

class Platos(models.Model):
    nombre = models.CharField(max_length=40, default='')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    procedencia = models.CharField(max_length=100, default='')
