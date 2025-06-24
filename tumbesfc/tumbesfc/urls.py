from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jugadores.views import JugadorViewSet
from partidos.views import PartidoViewSet
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from django.core.files.storage import default_storage


router = routers.DefaultRouter()
router.register(r'jugadores', JugadorViewSet)
router.register(r'partidos', PartidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),  # <-- Agrega esto
    path('jugadores/', include('jugadores.urls')),
    path('partidos/', include('partidos.urls')),
    path('noticias/', include('noticias.urls')),
    path('api/', include(router.urls)),
]
