from django.contrib import admin
from django.urls import path

from . import views

apps_name="cartas_app"


urlpatterns = [
    path('inicio-partida/', views.IniciarPartida),
    # path('duplicar/', views.duplicar_lista),
    path('barajar-sistema/', views.barajar_sistema),
    # path('repartir-cartas/', views.Repartir_Cartas),
]