from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias_list, name='noticias_list'),
    path('<int:pk>/', views.noticia_detalle, name='noticia_detalle'),

]
