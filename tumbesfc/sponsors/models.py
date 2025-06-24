from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage # <-- 1. Importar

s3_storage = S3Boto3Storage()

class Sponsor(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='sponsors/', storage=s3_storage)
    url = models.URLField('Sitio web o red social')
    destacado = models.BooleanField('¿Sponsor influyente?', default=False)

    def __str__(self):
        return self.nombre
