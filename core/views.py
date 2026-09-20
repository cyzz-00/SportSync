from django.http import HttpResponse

# Crear las funciones de vista para las páginas de inicio y acerca de sportSync
from django.shortcuts import render

def inicio(request):
    return render(request, "core/inicio.html")

def acerca(request):
    return render(request, "core/acercade.html")