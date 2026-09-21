from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from usuarios.decorators import roles_permitidos
from usuarios.models import Usuario

from .forms import ActividadForm
from .models import Actividad


@roles_permitidos(Usuario.Rol.ORGANIZADOR)
def panel_actividades_organizador(request):
    actividades = Actividad.objects.filter(
        organizador=request.user
    )

    return render(
        request,
        "actividades/panel_actividades_organizador.html",
        {"actividades": actividades},
    )


@roles_permitidos(Usuario.Rol.ORGANIZADOR)
@require_http_methods(["GET", "POST"])
def crear_actividad(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)

        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.organizador = request.user
            actividad.estado = Actividad.Estado.BORRADOR
            actividad.save()

            return redirect(
                "actividades:panel_actividades_organizador"
            )
    else:
        form = ActividadForm()

    return render(
        request,
        "actividades/formulario_actividad.html",
        {"form": form},
    )