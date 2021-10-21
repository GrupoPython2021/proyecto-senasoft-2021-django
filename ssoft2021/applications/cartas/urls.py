from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('inicio-partida/', views.InicioPartida.as_view()),
    # path('duplicar/', views.duplicar_lista),
    path('barajar-sistema/', views.barajar_sistema),
]