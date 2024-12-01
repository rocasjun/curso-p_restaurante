from django.urls import path
from .views import lista_meseros, lista_meseros_peruanos
from . import views

urlpatterns = [
    path('lista/', lista_meseros, name='lista_meseros'),
    path('lista_peruanos/', lista_meseros_peruanos, name='lista_meseros_peruanos'),
    path('actualizar_edades/', views.actualizar_edades, name='actualizar_edades'),
]