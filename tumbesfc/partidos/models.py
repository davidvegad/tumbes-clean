from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage # <-- 1. Importar

s3_storage = S3Boto3Storage()

class Partido(models.Model):
    liga = models.CharField(max_length=100, blank=True, null=True)
    equipo_rival = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    logo_visitante = models.ImageField(upload_to='logos_visitantes/', blank=True, null=True, storage=s3_storage)
    goles_local = models.PositiveSmallIntegerField("Goles Tumbes FC", default=0)
    goles_visitante = models.PositiveSmallIntegerField("Goles rival", default=0)
    goleadores_local = models.CharField("Goleadores Tumbes FC", max_length=250, blank=True)
    goleadores_visitante = models.CharField("Goleadores rival", max_length=250, blank=True)
    finalizado = models.BooleanField("¿Ya jugado?", default=False)

    def __str__(self):
        return f"{self.liga or ''}: Tumbes FC {self.goles_local or ''} - {self.goles_visitante or ''} {self.equipo_rival}"