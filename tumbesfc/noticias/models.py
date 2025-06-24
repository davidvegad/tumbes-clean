from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage # <-- 1. Importar

s3_storage = S3Boto3Storage()

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    resumen = models.TextField()
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', storage=s3_storage)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
