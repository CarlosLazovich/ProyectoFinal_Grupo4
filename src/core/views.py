from django.shortcuts import render
from publicaciones.models import Publicaciones


# view que renderiza la pagina de inicio
# renderiza las 4 ultimas publicaciones en el index
def indexView(request):
    posteos = Publicaciones.objects.order_by('-fecha')[0:4]
    ctx = {'posteos': posteos}
    return render(request, 'index.html', ctx)





