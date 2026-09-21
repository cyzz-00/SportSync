from django.shortcuts import render, redirect

from .forms import RegistroForm, SolicitudOrganizadorForm
from django.db import IntegrityError, transaction

from django.http import HttpResponse
from .decorators import roles_permitidos
from .models import Usuario, SolicitudOrganizador


## Vista para el registro de nuevos usuarios.

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("usuarios:registro_exitoso")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})



# Esta vista muestra un mensaje de éxito después de que un usuario se registra correctamente.



def registro_exitoso(request):
    return render(request, "usuarios/registro_exitoso.html")

@roles_permitidos(
    Usuario.Rol.ORGANIZADOR,
    Usuario.Rol.ADMINISTRADOR,
)


# Este decorador asegura que solo los usuarios con el rol de ORGANIZADOR o ADMINISTRADOR puedan acceder a esta vista.


def panel_organizador(request):
    return HttpResponse(
        "Acceso permitido: área de Organizador."
    )


# Este decorador asegura que solo los usuarios con el rol de ADMINISTRADOR puedan acceder a esta vista.

@roles_permitidos(Usuario.Rol.ADMINISTRADOR)
def panel_administrador(request):
    solicitudes = (
        SolicitudOrganizador.objects
        .filter(estado=SolicitudOrganizador.Estado.PENDIENTE)
        .select_related("participante")
        .order_by("fecha_solicitud")
    )

    return render(
        request,
        "usuarios/panel_administrador.html",
        {"solicitudes": solicitudes},
    )


# Este decorador asegura que solo los usuarios con el rol de PARTICIPANTE puedan acceder a esta vista.


@roles_permitidos(Usuario.Rol.PARTICIPANTE)
def panel_participante(request):
    solicitudes = SolicitudOrganizador.objects.filter(
        participante=request.user
    )

    tiene_pendiente = solicitudes.filter(
        estado=SolicitudOrganizador.Estado.PENDIENTE
    ).exists()

    form = SolicitudOrganizadorForm()

    if request.method == "POST":
        if tiene_pendiente:
            return redirect("usuarios:panel_participante")

        form = SolicitudOrganizadorForm(request.POST)

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.participante = request.user
            solicitud.estado = SolicitudOrganizador.Estado.PENDIENTE

            try:
                with transaction.atomic():
                    solicitud.save()
            except IntegrityError:
                # Evita duplicados si se envía dos veces a la vez.
                if not solicitudes.filter(
                    estado=SolicitudOrganizador.Estado.PENDIENTE
                ).exists():
                    raise

            return redirect("usuarios:panel_participante")

    ultima_solicitud = solicitudes.order_by(
        "-fecha_solicitud"
    ).first()

    return render(
        request,
        "usuarios/panel_participante.html",
        {
            "solicitud": ultima_solicitud,
            "form": form,
            "tiene_pendiente": tiene_pendiente,
        },
    )