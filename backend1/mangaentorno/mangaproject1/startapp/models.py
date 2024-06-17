from django.db import models
from django.contrib.auth.models import User  # Importación corregida

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    bith_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Manga(models.Model):
    idManga = models.CharField(max_length=13, primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.estado} {self.author.name} {self.author.last_name}"

class TipoSubscripcion(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Subscripcion(models.Model):
    tipo = models.ForeignKey(TipoSubscripcion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usando la importación correcta
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo.nombre}"  # Corrección en la referencia a `username`
