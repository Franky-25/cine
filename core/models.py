from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

# python manage.py makemigratioms --- lee el archivo models y crea un archivo de migracion
# python manage.py migrate ---- toma las migraciones pendientes y volcarlas contra la BBDD
# python manage.py createsuperuser --- crea super usuario administrador        


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField()
    anio = models.IntegerField(verbose_name="Año")
    genero =models.ForeignKey(Genero,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
