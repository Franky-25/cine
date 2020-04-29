from django.contrib import admin
from .models import Genero, Pelicula

# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion', 'anio', 'genero']
    search_fields = ['nombre', 'anio']
    list_filter = ['genero']
    list_per_page = 7


admin.site.register(Genero)
admin.site.register(Pelicula, PeliculasAdmin)