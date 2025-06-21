from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    resumen = models.TextField()
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
