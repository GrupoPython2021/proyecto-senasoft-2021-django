from django.db import models

# from ssoft2021.applications.sesion.models import Sesion

from .views import IniciarPartida

class CartaManager(models.Manager):

    def buscar_sala(self, sesioncod):

        resultado = self.filter(sesion=sesioncod)

        print(resultado)

        return resultado

    