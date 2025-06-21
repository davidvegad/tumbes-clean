from django.shortcuts import render
from .models import Noticia

def noticias_list(request):
    noticias = Noticia.objects.order_by('-fecha')[:8]
    return render(request, 'noticias/noticias.html', {'noticias': noticias})
