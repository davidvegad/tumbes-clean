from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.nombre
