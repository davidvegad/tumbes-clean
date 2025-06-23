from rest_framework import viewsets
from django.shortcuts import render
from .models import Jugador
from partidos.models import Partido
from .serializers import JugadorSerializer
from datetime import date
from noticias.models import Noticia
from sponsors.models import Sponsor
from home.models import HeroSlide


class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer



def equipo(request):
    jugadores = Jugador.objects.all()
    proximos_partidos = Partido.objects.filter(fecha__gte=date.today()).order_by('fecha', 'hora')[:5]
    resultados = Partido.objects.filter(finalizado=True).order_by('-fecha')[:6]  # Últimos 6 jugados
    noticias = Noticia.objects.order_by('-fecha')[:4]  # Muestra las 4 más recientes
    sponsors_destacados = Sponsor.objects.filter(destacado=True)
    sponsors_normales = Sponsor.objects.filter(destacado=False)
    slides = HeroSlide.objects.all()

    return render(request, 'jugadores/equipo.html', {
        'jugadores': jugadores,
        'proximos_partidos': proximos_partidos,
        'resultados': resultados,
        'noticias': noticias,
        'sponsors_destacados': sponsors_destacados,
        'sponsors_normales': sponsors_normales,
        'slides': slides,
    })