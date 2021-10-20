from django.db import models
#import timestampedmodels
from model_utils.models import TimeStampedModel


class Sesion(TimeStampedModel):
    """Modelo para Sesion."""

    sesion = models.CharField(max_length=5)

    class Meta:
        """Meta para Sesion."""

        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'

    def __str__(self):
        """Representacion de Sesion."""
        return self.sesion

