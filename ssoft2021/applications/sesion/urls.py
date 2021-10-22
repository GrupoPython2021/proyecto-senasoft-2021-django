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
        'unirse_partida/', 
        views.CrearSalaView.as_view(), 
        name='crear'
    ),
    path( 
        'partida2/', 
        views.iniciar, 
        name='partida2'
    ),
]