from django.urls import path
from .views import lista_meseros, lista_meseros_peruanos, meseros_mayores
from . import views
from .views import CrearMeseroView, EditarMeseroView, EliminarMeseroView

from .views import crear_mesero, editar_mesero, obtener_mesero_detalle, eliminar_mesero

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('lista/', lista_meseros, name='lista_meseros'),
    path('lista_peruanos/', lista_meseros_peruanos, name='lista_meseros_peruanos'),
    path('actualizar_edades/', views.actualizar_edades, name='actualizar_edades'),
    path('mayores/', meseros_mayores, name='meseros_mayores'),
    path('crear/', CrearMeseroView.as_view(), name='crear_mesero'),
    #path('lista_peruanos/', ListarMeserosPeruanosView.as_view(), name='lista_meseros_peruanos'),
    path('editar/<int:pk>/', EditarMeseroView.as_view(), name='editar_mesero'),
    path('eliminar/<int:pk>/', EliminarMeseroView.as_view(), name='eliminar_mesero'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/meseros/crear/', crear_mesero, name='crear_mesero_api'),
    path('api/meseros/editar/<int:pk>/', editar_mesero, name='editar_mesero_api'),
    path('api/meseros/detalle/<int:pk>/', obtener_mesero_detalle, name='detalle_mesero_api'),
    path('api/meseros/eliminar/<int:pk>/', eliminar_mesero, name='eliminar_mesero_api'),
]


