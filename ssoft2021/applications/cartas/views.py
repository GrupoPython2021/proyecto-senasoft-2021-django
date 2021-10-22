from django.shortcuts import render

from django.views.generic import TemplateView

from django.http import HttpResponse, request

# Import para selecciones aleatorias
import random

from applications.users.models import User 
from applications.sesion.models import Sesion 
# from applications.sesion.models import Cartas_Completas 


""" Vist genérica TemplateView 
basda en clase """
#class InicioPartida(TemplateView):
#   context_object_name = 'usuario'
#   template_name = "cartas/iniciar-partida.html"

def IniciarPartida(request):
    sesioncod = Sesion.objects.last()

    consulta=Sesion.objects.filter(sesion=sesioncod)
    # for i in range(User.objects.len()):
    # consul_user=Sesion.objects.filter(sesion=sesioncod).get()

    

    #return HttpResponse('23')
    return render(request, "cartas/pantalla-juego.html", 
    {'sesioncod':sesioncod,
    'consulta':consulta,
    # 'consul_user': consul_user
    })

# def buscar_codigo():
#     palabra_clave= IniciarPartida(request)
#     print(palabra_clave)



""" Listas de las Cartas """
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


""" Función para barajar cartas 
y repartir al sis """
def barajar_sistema(request):
    # duplicar listas
    PROGRAMADORESCP = PROGRAMADORES[:]
    MODULOSCP = MODULOS[:]
    T_ERRORCP = T_ERROR[:]

    cartas_sis = [] # nuevo arreglo para cartas del sistema
    # función choice para seleccionar una carta aleatoria
    sis1 = random.choice(PROGRAMADORESCP) 
    sis2 = random.choice(MODULOSCP)
    sis3 = random.choice(T_ERRORCP)

    # eliminar cartas seleccionadas en el duplicado
    PROGRAMADORESCP.remove(sis1)
    MODULOSCP.remove(sis2)
    T_ERRORCP.remove(sis3)

    # agregar cartas al nuevo arreglo
    cartas_sis.append(sis1[1])
    cartas_sis.append(sis2[1])
    cartas_sis.append(sis3[1])

    """ llamado función baraja_jugador para 
    enviar copia listas y ejecutarla""" 
    barajar_jugador(request, PROGRAMADORESCP, MODULOSCP, T_ERRORCP)
    #Repartir_Cartas()
    # return (render)
    return HttpResponse(""" Hola Mundo """)

    

""" Función para revolver y repartir cartas a los jugadores """
def barajar_jugador(request, PROGRAMADORESCP, MODULOSCP, T_ERRORCP):
    # mazo para cada jugador
    jugador1=[] 
    jugador2=[]
    jugador3=[]
    jugador4=[]

    total_cartas=[] # lista para barajar las cartas

    # Bucles para añadir cartas a baraja
    for i in range(6):
        total_cartas.append(PROGRAMADORESCP[i][1])
    for i in range(5):
        total_cartas.append(MODULOSCP[i][1])
        total_cartas.append(T_ERRORCP[i][1])
    
    # Bucles para repartir cartas aleatoreamente
    for i in range(4):
        for j in range(4):
            if i == 0:
                jug = random.choice(total_cartas) # seleccionar cartas de la baraja
                total_cartas.remove(jug)
                jugador1.append(jug) # añadir carta seleccionada a lista
        for k in range(4):
            if i == 1:
                jug = random.choice(total_cartas)
                total_cartas.remove(jug)
                jugador2.append(jug) 
        for l in range(4):
            if i == 2:
                jug = random.choice(total_cartas) 
                total_cartas.remove(jug)
                jugador3.append(jug) 
        for m in range(4):
            if i == 3:
                jug = random.choice(total_cartas) 
                total_cartas.remove(jug)
                jugador4.append(jug)
    
def Retomar_Partida(request):
    #captura de nickname
    nick2 = request.GET['nick']
    cod_sesion = request.GET['cod_sesion']

    return render(request, "cartas/pantalla-juego2.html",
    {'nick2': nick2,
    'cod_sesion':cod_sesion}) 

def Unirse_Sesion(request):
    #nick2 = request.GET['nick']
    #cod_sesion = request.GET['cod_sesion']

    return render(request, "cartas/pantalla-juego2.html") 






# def Repartir_Cartas():
#     # barajar_sistema(request)
#     codigo_sala = request.GET.get("codigo", '')
    
#     # return Carta.

