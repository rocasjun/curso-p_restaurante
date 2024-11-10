from django.db import models

class Meseros(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=30, default='')
    edad = models.IntegerField(default=0)
