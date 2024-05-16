from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def index(request):
    return render(request, 'peliculas/index.html')