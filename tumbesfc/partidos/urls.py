from django.urls import path
from . import views

urlpatterns = [
    path('proximos/', views.proximos_partidos, name='proximos_partidos'),
]
