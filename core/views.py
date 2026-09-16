from django.http import HttpResponse


def inicio(request):
    return HttpResponse(
        "<h1><center>SportSync</h1>"
        "<p>Sistema de Gestión de Actividades y Torneos Deportivos Amateur.</p>"
        "<p>Mi primer proyecto Django está funcionando correctamente.</p>"
        '<a href="/acerca/">Acerca del proyecto</a>'
    )

def acerca(request):
    return HttpResponse(
        "<h1><center>Acerca de SportSync</h1>"
        "<p>Proyecto desarrollado para la asignatura Desarrollo de Software V.</p>"
        "<p>Su objetivo es facilitar la organización de actividades deportivas, "
        "la inscripción de participantes y el control de asistencia.</p>"
        '<a href="/">Volver al inicio</a>'
    )