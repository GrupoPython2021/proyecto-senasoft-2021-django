from django.db import models

# Import para selecciones aleatorias
import random
# from django.db.models.fields.files import ImageFieldFile

#import timestampedmodels
from model_utils.models import TimeStampedModel
#import de user
from applications.users.models import User

# importar managers
from .managers import CartaManager


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
        ('8','Nómina'),
        ('9','Facturación'),
        ('10','Recibos'),
        ('11','Comprobante contable'),
        ('12','Usuarios'),
        ('13','Contabilidad'),
    ]

    T_ERROR = [
        ('14','404'),
        ('15','Stack overflow'),
        ('16','Memory out of range'),
        ('17','Null pointer'),
        ('18','Syntax error'),
        ('19','Encoding error'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    programadores = models.CharField(max_length=50, choices=PROGRAMADORES)
    modulo = models.CharField(max_length=50, choices=MODULOS)
    t_error = models.CharField(max_length=50, choices=T_ERROR)
    carta_repetida = models.CharField(max_length=50 )

    objects = CartaManager()

    class Meta:
        """Meta definition for Carta."""

        verbose_name = 'Cartas_jugador'
        verbose_name_plural = 'Cartas jugadores'

    def __str__(self):
        """Unicode representation of Carta."""
        pass


class Cartas_Completas(models.Model):
    """ Total de cartas: 19 """

    imagen_carta = models.ImageField(
        upload_to='Cartas_Completas', blank=True, null=False
    )

    # cartas_jugador = models.ForeignKey(
    #     Carta, on_delete=models.CASCADE,
    #     null=True
    # )
    
    class Meta:
        """Meta definition for Carta."""

        verbose_name = 'Cartas Completas'
        verbose_name_plural = 'Cartas Completas'

    def __str__(self):
        """Unicode representation of Carta."""
        return str(self.id)