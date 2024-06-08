from django.shortcuts import render

# Create your views here.

def pagina_inicio_view(request):
    return render(request, 'pagina_inicio.html')

def biografia_view(request):
    return render(request, 'biografia.html')

def proyectos_view(request):
    return render(request, 'proyectos.html')