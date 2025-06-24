from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage # <-- 1. Importar

s3_storage = S3Boto3Storage()


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='team/', blank=True, null=True, storage=s3_storage)

    def __str__(self):
        return self.nombre
