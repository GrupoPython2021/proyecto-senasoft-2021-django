from django.contrib import admin
from django.urls import path

from . import views

apps_name="cartas_app"


urlpatterns = [
    path(
        'inicio-partida/', 
        views.IniciarPartida
    ),
    # path('duplicar/', views.duplicar_lista),
    path(
        'barajar-sistema/', 
        views.barajar_sistema
    ),
    #
    path(
        'retomar_partida/', 
        views.Retomar_Partida, 
        name='retomar'
    ),
    path(
        'unirse_sesion/', 
        views.Unirse_Sesion, 
        name='unirse'
    ),
    path(
        'modal_acusar/',
        views.modal_acusar.as_view(),
        name='modal-acusar'
    ),
]