from typing import Any
from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True, blank=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción", null=True)

    def __str__(self):
        fila = str(self.id) + " - " + self.titulo + " - " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete()
        super().delete()