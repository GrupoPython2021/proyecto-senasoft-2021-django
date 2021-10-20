from django.db import models
#import timestampedmodels
from model_utils.models import TimeStampedModel
#impoort de sesion
from applications.sesion.models import Sesion


class User(TimeStampedModel):
    """Modelo para User."""

    username = models.CharField(max_length=15)
    activo = models.BooleanField()
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    

    class Meta:
        """Meta para User."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """Representation para User."""
        return self.username


