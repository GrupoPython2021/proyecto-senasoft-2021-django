import random

from jinja2 import Environment, FileSystemLoader
from django.shortcuts import render



#import view.generic
from django.views.generic import FormView, TemplateView

from django.http import HttpResponse

#import forms.forms
from .forms import CreateSalaViewForm
from .models import Sesion
from applications.users.models import User

#Vista de home
class HomeView(TemplateView):
    template_name = "home/home.html"

#vista iniciar aprtida

 


class CrearSalaView(FormView):
    template_name = "sesion/crear_sala.html"
    form_class = CreateSalaViewForm
    success_url = "sesion/partida1.html"

    casa={'1':'casa'}

    env = Environment(loader=FileSystemLoader("C:\\Users\\mwmar\\Desktop\\ss\\proyecto-senasoft-2021-django\\ssoft2021\\templates\\cartas"))
    template = env.get_template("iniciar-partida.html")
    html = template.render(casa)




  #  form.cleaned_data['my_form_field_name']


def crear(request):
    return render(request, "sesion/partida1.html")


def iniciar(request):
    
    #captura del nickname
    nick = request.GET['nick']
    #numero de dos digitos aleatorios
    b = random.randint(10, 99)
    #nickname y clavepersonal
    nickname = nick + "-" + str(b)
    
    #nuemero hexadecimal aleatorio
    r = lambda: random.randint(90000,99999)
    r = str('%02X' % (r()))

    #guardado de la sesion en la base de datos
    Sesion.objects.create(sesion=r)
    print(Sesion.objects.all())
    #print(nick)
    print(r)

    User.objects.create(username=nick, activo=True, sesion=(Sesion.objects.last()))
    
    mensaje = 'Su nombre de usuario es: {}, \
        y el codigo de la sesion es {}'.format(nickname,r)

    print(nick)
    print(r)

    #return HttpResponse(mensaje)
    return render(request, "cartas/iniciar-partida.html")








