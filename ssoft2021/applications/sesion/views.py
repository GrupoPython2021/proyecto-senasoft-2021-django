from django.shortcuts import render

#import view.generic
from django.views.generic import FormView, TemplateView

from django.http import HttpResponse



#Vista de home
class HomeView(TemplateView):
    template_name = "home/home.html"

#vista iniciar aprtida

class CrearSalaView(TemplateView):
    template_name = "sesion/crear_sala.html"
    #
    def username(request):
        if request.method == 'POST':
            nickname = request.POST.get('nickname')
            correo = nickname
            print(correo)

        return render(request, 'sesion/crear_sala.html', {})








