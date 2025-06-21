from rest_framework import viewsets
from django.shortcuts import render
from .models import Jugador
from partidos.models import Partido
from .serializers import JugadorSerializer
from datetime import date
from noticias.models import Noticia


class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer



def equipo(request):
    jugadores = Jugador.objects.all()
    proximos_partidos = Partido.objects.filter(fecha__gte=date.today()).order_by('fecha', 'hora')[:5]
    noticias = Noticia.objects.order_by('-fecha')[:4]  # Muestra las 4 más recientes
    return render(request, 'jugadores/equipo.html', {
        'jugadores': jugadores,
        'proximos_partidos': proximos_partidos,
        'noticias': noticias,
    })