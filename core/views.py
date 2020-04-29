from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from rest_framework import viewsets
from .serializers import PeliculaSerializer
# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def galeria(request):
    return render(request, 'core/galeria.html')


def listado_pelicula(request):
    peliculas = Pelicula.objects.all()
    data = {
        'peliculas': peliculas
    }
    return render(request, 'core/listado_peliculas.html', data)

@permission_required('core.add_pelicula')
def nueva_pelicula(request):
    data = {
        'form':PeliculaForm()
    }
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request, 'core/nueva_pelicula.html', data)   

def modificar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    data = {
        'form' : PeliculaForm(instance=pelicula)
    }     

    if request.method == 'POST':
        formulario = PeliculaForm(data=request.POST, instance=pelicula  )
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario
    return render(request, 'core/modificar_pelicula.html',data)

def elimminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()

    return redirect(to="listado_peliculas")   


def registro_usuario(request):
    data = {
        'form' : CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to = 'home')

    return render(request, 'registration/registrar.html', data)     
    

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer