from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('inicio-partida/', views.InicioPartida.as_view()),
    path('barajar-sistema/', views.barajar_sistema),
]