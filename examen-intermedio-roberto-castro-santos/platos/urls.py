from django.urls import path
from .views import lista_platos
from . import views

urlpatterns = [
    path('lista/', lista_platos, name='lista_platos'),
    path('eliminar_platos_bajos_precio/', views.eliminar_platos_bajos_precio, name='eliminar_platos_bajos_precio'),
]
