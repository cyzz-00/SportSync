from django.shortcuts import render, redirect

from .forms import RegistroForm

from django.http import HttpResponse
from .decorators import roles_permitidos
from .models import Usuario


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("usuarios:registro_exitoso")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})


def registro_exitoso(request):
    return render(request, "usuarios/registro_exitoso.html")

@roles_permitidos(
    Usuario.Rol.ORGANIZADOR,
    Usuario.Rol.ADMINISTRADOR,
)
def panel_organizador(request):
    return HttpResponse(
        "Acceso permitido: área de Organizador."
    )

@roles_permitidos(Usuario.Rol.ADMINISTRADOR)
def panel_administrador(request):
    return HttpResponse(
        "Acceso permitido: área de Administrador."
    )