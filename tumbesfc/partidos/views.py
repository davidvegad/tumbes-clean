from rest_framework import viewsets
from .models import Partido
from .serializers import PartidoSerializer
from django.shortcuts import render
from datetime import date


class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

def proximos_partidos(request):
    # Solo muestra partidos a partir de hoy (puedes personalizar el filtro)
    partidos = Partido.objects.filter(fecha__gte=date.today()).order_by('fecha', 'hora')
    return render(request, 'partidos/proximos.html', {'partidos': partidos})