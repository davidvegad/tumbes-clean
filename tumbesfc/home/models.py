from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage # <-- 1. Importar

s3_storage = S3Boto3Storage()

class HeroSlide(models.Model):
    imagen = models.ImageField(upload_to='hero/', storage=s3_storage)
    titulo = models.CharField(max_length=100, blank=True)
    subtitulo = models.CharField(max_length=200, blank=True)
    boton_texto = models.CharField(max_length=50, blank=True)
    link = models.URLField('Enlace destino', blank=True)
    orden = models.PositiveIntegerField(default=0, help_text='Para ordenar los slides')

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo or f"Slide {self.pk}"