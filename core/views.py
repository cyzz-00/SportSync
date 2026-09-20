from django.http import HttpResponse

# Crear las funciones de vista para las páginas de inicio y acerca de sportSync
from django.shortcuts import render

def inicio(request):
    return render(request, "core/inicio.html")

def acerca(request):
    return HttpResponse(
        "<h1><center>Acerca de SportSync</h1>"
        "<p>Proyecto desarrollado para la asignatura Desarrollo de Software V.</p>"
        "<p>Su objetivo es facilitar la organización de actividades deportivas, "
        "la inscripción de participantes y el control de asistencia.</p>"
        '<a href="/">Volver al inicio</a>'
    )