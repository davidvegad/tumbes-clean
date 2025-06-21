from django.db import models

class Sponsor(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='sponsors/')
    url = models.URLField('Sitio web o red social')
    destacado = models.BooleanField('¿Sponsor influyente?', default=False)

    def __str__(self):
        return self.nombre
