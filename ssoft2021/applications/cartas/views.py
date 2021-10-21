from django.shortcuts import render

from django.views.generic import TemplateView

from django.http import HttpResponse


# Import para selecciones aleatorias
import random
# Create your views here.




class InicioPartida(TemplateView):
    template_name = "cartas/iniciar-partida.html"
    


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



def barajar_sistema(request):
    # función choice para seleccionar una carta aleatoria
    
    cartas_sis = [] # nuevo arreglo para cartas del sistema
    sis1 = random.choice(PROGRAMADORES) 
    sis2 = random.choice(MODULOS)
    sis3 = random.choice(T_ERROR)

    PROGRAMADORES.remove(sis1)
    MODULOS.remove(sis2)
    T_ERROR.remove(sis3)
    
    # agregar cartas al nuevo arreglo
    cartas_sis.append(sis1[1])
    cartas_sis.append(sis2[1])
    cartas_sis.append(sis3[1])
    print(cartas_sis)
    return HttpResponse(""" Hola Mundo """)

    



def barajar_jugador(self):
    jugador1=[]
    jugador2=[]
    jugador3=[]
    jugador4=[]

    total_cartas=[] # lista para barajar las cartas
    # bucles para añadir cartas a baraja
    for i in range(6):
        total_cartas.append(self.PROGRAMADORES[i][1])
    for i in range(5):
        total_cartas.append(self.MODULOS[i][1])
        total_cartas.append(self.T_ERROR[i][1])

    # cartas_jugador=[] # nueva lista para cartas jugadores
    for i in range(4):
        for j in range(4):
            if i == 0:
                jug = random.choice(total_cartas) # seleccionar cartas de la baraja
                total_cartas.remove(jug)
                jugador1.append(jug) # añadir carta seleccionada a lista
        for k in range(4):
            if i == 1:
                jug = random.choice(total_cartas) # seleccionar cartas de la baraja
                total_cartas.remove(jug)
                jugador2.append(jug) # añadir carta seleccionada a lista
        for l in range(4):
            if i == 2:
                jug = random.choice(total_cartas) # seleccionar cartas de la baraja
                total_cartas.remove(jug)
                jugador3.append(jug) # añadir carta seleccionada a lista
        for m in range(4):
            if i == 3:
                jug = random.choice(total_cartas) # seleccionar cartas de la baraja
                total_cartas.remove(jug)
                jugador4.append(jug) # añadir carta seleccionada a lista