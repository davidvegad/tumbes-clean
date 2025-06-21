from django.db import models

class Partido(models.Model):
    equipo_rival = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)

    def __str__(self):
        return f"Tumbes FC vs {self.equipo_rival} ({self.fecha})"
