from django.db import models


class CartaManager(models.Manager):

    def codigo_tb_sesion(self):
        return self.filter()