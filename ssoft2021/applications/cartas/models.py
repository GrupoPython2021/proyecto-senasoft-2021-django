from django.db import models

# Import para selecciones aleatorias
import random
from django.db.models.fields.files import ImageFieldFile

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
    carta_repetida = models.CharField(max_length=50 )

    class Meta:
        """Meta definition for Carta."""

        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'

    def __str__(self):
        """Unicode representation of Carta."""
        pass


class Cartas_Completas(models.Model):
    """ Total de cartas: 19 """

    imagen_carta = models.ImageField(
        upload_to='Cartas_Completas', blank=True, null=False
    )

    cartas_jugador = models.ForeignKey(
        Carta, on_delete=models.CASCADE
    )
    
    def __str__(self):
        """Unicode representation of Carta."""
        pass