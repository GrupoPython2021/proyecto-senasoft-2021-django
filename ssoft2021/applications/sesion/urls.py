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
        'crear-partida/', 
        views.CrearSalaView.as_view(), 
        name='crear'
    ),
]