from django.shortcuts import render, redirect
from .models import Pelicula

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def crear(request):
    return render(request, 'peliculas/crear.html')

def editar(request):
    return render(request, 'peliculas/editar.html')

def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('index')