from django.db import models

#import timestampedmodels
from model_utils.models import TimeStampedModel
#import de user
from applications.users.models import User


class Carta(models.Model):
    """Modelo Carta."""

    PROGRAMADORES = [
        ('1','Pedro'),
        ('2','Juan'),
        ('3','Carlos'),
        ('4','Juanita'),
        ('5','Antonio'),
        ('6','Carolina'),
        ('7','Manuel'),
    ]

    MODULOS = [
        ('1','Nómina'),
        ('2','Facturación'),
        ('3','Recibos'),
        ('4','Comprobante contable'),
        ('5','Usuarios'),
        ('6','Contabilidad'),
    ]

    T_ERROR = [
        ('1','404'),
        ('2','Stack overflow'),
        ('3','Memory out of range'),
        ('4','Null pointer'),
        ('5','Syntax error'),
        ('6','Encoding error'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    programadores = models.CharField(max_length=50, choices=PROGRAMADORES)
    modulo = models.CharField(max_length=50, choices=MODULOS)
    t_error = models.CharField(max_length=50, choices=T_ERROR)


    class Meta:
        """Meta definition for Carta."""

        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'

    def __str__(self):
        """Unicode representation of Carta."""
        pass

