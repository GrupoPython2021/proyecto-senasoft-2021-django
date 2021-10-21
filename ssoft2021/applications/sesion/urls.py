#imoport Path
from django.urls import path

from . import views

app_name = 'sesion_app'

urlpatterns = [
    path(
        '', 
        views.HomeView.as_view(), 
        name='home'
    ),
    path(
        'crear_partida/', 
        views.CrearSalaView.as_view(), 
        name='crear'
    ),
    path(
        'partida1/', 
        views.crear, 
        name='partida1'
    ),
    path(
        'partida2/', 
        views.iniciar, 
        name='partida2'
    ),
]