from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jugadores.views import JugadorViewSet
from partidos.views import PartidoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'jugadores', JugadorViewSet)
router.register(r'partidos', PartidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jugadores/', include('jugadores.urls')),
    path('partidos/', include('partidos.urls')),
    path('noticias/', include('noticias.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
