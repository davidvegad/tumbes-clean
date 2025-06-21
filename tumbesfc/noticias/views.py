from django.shortcuts import render, get_object_or_404
from .models import Noticia

def noticias_list(request):
    noticias = Noticia.objects.order_by('-fecha')[:8]
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def noticia_detalle(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/noticia_detalle.html', {'noticia': noticia})