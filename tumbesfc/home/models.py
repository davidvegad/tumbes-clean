from django.db import models

class HeroSlide(models.Model):
    imagen = models.ImageField(upload_to='hero/')
    titulo = models.CharField(max_length=100, blank=True)
    subtitulo = models.CharField(max_length=200, blank=True)
    boton_texto = models.CharField(max_length=50, blank=True)
    link = models.URLField('Enlace destino', blank=True)
    orden = models.PositiveIntegerField(default=0, help_text='Para ordenar los slides')

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo or f"Slide {self.pk}"