from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def crear(request):
    formulario = PeliculaForm(request.POST, request.FILES)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request, 'peliculas/crear.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'peliculas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('index')