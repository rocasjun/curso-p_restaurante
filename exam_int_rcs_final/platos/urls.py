from django.urls import path
from .views import lista_platos, platos_precios_altos
from . import views

urlpatterns = [
    path('lista/', lista_platos, name='lista_platos'),
    path('eliminar_platos_bajos_precio/', views.eliminar_platos_bajos_precio, name='eliminar_platos_bajos_precio'),
    path('precios_altos/', platos_precios_altos, name='platos_precios_altos'),
]
