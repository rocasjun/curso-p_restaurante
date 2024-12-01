from django.shortcuts import render

from .models import Platos
from django.http import HttpResponse

def lista_platos(request):
    if not Platos.objects.filter(procedencia='Perú', precio__gt=40).exists():
        Platos.objects.create(nombre='Ceviche', precio=45.00, procedencia='Perú')
        Platos.objects.create(nombre='Lomo Saltado', precio=50.00, procedencia='Perú')
        Platos.objects.create(nombre='Ají de Gallina', precio=55.00, procedencia='Perú')

    #platos_peruanos = Platos.objects.filter(procedencia='Perú', precio__gt=40)
    platos_peruanos = Platos.objects.all()
    
    return render(request, 'platos/lista_platos.html', {'platos': platos_peruanos})
    #platos = Platos.objects.all()
    #return render(request, 'platos/lista_platos.html', {'platos': platos})

def eliminar_platos_bajos_precio(request):
    platos_eliminados, _ = Platos.objects.filter(precio__lt=15).delete()
    
    return HttpResponse(f"{platos_eliminados} platos eliminados con un precio menor a 15 soles.")
