from django.shortcuts import render
from .models import Meseros
from django.db import models
from django.http import HttpResponse

def lista_meseros(request):
    meseros = Meseros.objects.all()
    
    return render(request, 'meseros/lista_meseros.html', {'meseros': meseros})

def lista_meseros_peruanos(request):
    meseros_peruanos = Meseros.objects.filter(nacionalidad='Perú', edad__lt=30)
    
    return render(request, 'meseros/lista_meseros_peruanos.html', {'meseros': meseros_peruanos})

def actualizar_edades(request):
    Meseros.objects.all().update(edad=models.F('edad') + 5)
    
    return HttpResponse("Edades de los meseros actualizadas en 5 años.")