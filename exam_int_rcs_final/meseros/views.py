from django.shortcuts import render
from .models import Meseros
from django.db import models
from django.http import HttpResponse
from django.http import JsonResponse
from .serializers import MeserosSerializer
from rest_framework.decorators import api_view
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

def lista_meseros(request):
    meseros = Meseros.objects.all()
    
    return render(request, 'meseros/lista_meseros.html', {'meseros': meseros})

def lista_meseros_peruanos(request):
    meseros_peruanos = Meseros.objects.filter(nacionalidad='Perú', edad__lt=30)
    
    return render(request, 'meseros/lista_meseros_peruanos.html', {'meseros': meseros_peruanos})

def actualizar_edades(request):
    Meseros.objects.all().update(edad=models.F('edad') + 5)
    
    return HttpResponse("Edades de los meseros actualizadas en 5 años.")

@api_view(['GET'])
def meseros_mayores(request):
    meseros = Meseros.objects.filter(edad__gt=25)
    serializer = MeserosSerializer(meseros, many=True)
    return JsonResponse(serializer.data, safe=False)

class CrearMeseroView(CreateView):
    model = Meseros
    fields = ['nombre', 'nacionalidad', 'edad', 'dni']
    template_name = 'meseros/crear_mesero.html'
    success_url = reverse_lazy('lista_meseros_peruanos')

@api_view(['POST'])
def crear_mesero(request):
    serializer = MeserosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarMeseroView(UpdateView):
    model = Meseros
    fields = ['nombre', 'nacionalidad', 'edad', 'dni']
    template_name = 'meseros/editar_mesero.html'
    success_url = reverse_lazy('lista_meseros_peruanos')

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def editar_mesero(request, pk):
    mesero = get_object_or_404(Meseros, pk=pk)
    serializer = MeserosSerializer(mesero, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_mesero_detalle(request, pk):
    mesero = get_object_or_404(Meseros, pk=pk)
    serializer = MeserosSerializer(mesero)
    return Response(serializer.data, status=status.HTTP_200_OK)

class EliminarMeseroView(DeleteView):
    model = Meseros
    template_name = 'meseros/eliminar_mesero.html'
    success_url = reverse_lazy('lista_meseros_peruanos')
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_mesero(request, pk):
    mesero = get_object_or_404(Meseros, pk=pk)
    mesero.delete()
    return Response({'message': 'Mesero eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
