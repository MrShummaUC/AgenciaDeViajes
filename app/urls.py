from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('base/', base, name='base'),
    path('', cliente, name='cliente'),
    path('contrato/', contrato, name='contrato'),
    path('deposito/', deposito, name='deposito'),
    path('estado/', estado, name='estado'),
    path('monto/', monto, name='monto'),
    path('perfil/', perfil, name='perfil'),
    path('reporte/', reporte, name='reporte'),
    path('ContratoCliente/', ContratoCliente, name='ContratoCliente'),
    path('ContratoSeguro/', ContratoSeguro, name='ContratoSeguro'),
    path('meta/', meta, name='meta'),
    path('Publicaciones/', Publicaciones, name='Publicaciones'),
    path('seguro/', seguro, name='seguro'),
    path('ServicioContratado/', ServicioContratado, name='ServicioContratado'),
    path('ServiciosAdicionales/', ServiciosAdicionales, name='ServiciosAdicionales'),
]