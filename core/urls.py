
from django.urls import path, include
from .views import home
from .views import galeria
from .views import listado_pelicula
from .views import nueva_pelicula
from .views import modificar_pelicula
from .views import elimminar_pelicula
from .views import registro_usuario
from .views import PeliculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('peliculas', PeliculaViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"), 
    path('listado-peliculas/', listado_pelicula, name="listado_peliculas"),
    path('nueva-pelicula', nueva_pelicula, name="nueva_pelicula"),
    path('modificar-pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar-pelicula/<id>/', elimminar_pelicula, name="eliminar_pelicula"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('api/', include(router.urls)), 

]