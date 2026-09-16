from django.http import HttpResponse


def inicio(request):
    return HttpResponse(
        "<h1>SportSync</h1>"
        "<p>Sistema de Gestión de Actividades y Torneos Deportivos Amateur.</p>"
        "<p>Mi primer proyecto Django está funcionando correctamente.</p>"
    )