from django.shortcuts import render, redirect, get_object_or_404
main
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

# Importamos nuestros modelos y forms
from .models import Actividad
from .forms import ActividadForm

# Importamos el decorador personalizado de la app usuarios
from usuarios.decorators import roles_permitidos
from usuarios.models import Usuario

def lista_actividades(request):
    """
    Vista pública: Muestra todas las actividades PUBLICADAS.
    Cualquier persona puede verla (logueada o no).
    """
    ahora = timezone.now()
    # Filtramos: Solo publicadas Y que su fecha sea mayor o igual a hoy (opcional)
    actividades = Actividad.objects.filter(
        estado=Actividad.Estado.PUBLICADA
    ).order_by('fecha', 'hora')
    
    return render(request, 'actividades/lista.html', {'actividades': actividades})

@roles_permitidos(Usuario.Rol.ORGANIZADOR)
def crear_actividad(request):
    """
    Vista protegida: Solo Organizadores aprobados pueden crear.
    """
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            # Guardamos pero no commit todavía para añadir datos extra
            actividad = form.save(commit=False)
            actividad.organizador = request.user # Asignamos el dueño
            actividad.estado = Actividad.Estado.BORRADOR # Estado inicial
            
            actividad.save()
            return redirect('actividades:lista') # Redirigir a la lista (o al detalle)
    else:
        form = ActividadForm()
    
    return render(request, 'actividades/crear.html', {'form': form})

@login_required
def detalle_actividad(request, pk):
    """
    Muestra el detalle de una actividad.
    Lógica para calcular cupos disponibles.
    """
    actividad = get_object_or_404(Actividad, pk=pk)
    
    # Calculamos cuántos inscritos hay (Asumiendo que tendrás un modelo Inscripcion luego)
    # Por ahora usamos count() en una relación inversa que crearemos después
    # inscritos_count = actividad.inscripciones.count() 
    inscritos_count = 0 # Temporal hasta crear el modelo Inscripcion
    
    cupos_disponibles = actividad.cupo_maximo - inscritos_count
    esta_llena = cupos_disponibles <= 0
    
    contexto = {
        'actividad': actividad,
        'cupos_disponibles': cupos_disponibles,
        'esta_llena': esta_llena,
    }
    return render(request, 'actividades/detalle.html', contexto)

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







@roles_permitidos(Usuario.Rol.ORGANIZADOR)
@require_http_methods(["GET", "POST"])
def editar_actividad(request, actividad_id):
    actividad = get_object_or_404(
        Actividad,
        pk=actividad_id,
        organizador=request.user,
        estado=Actividad.Estado.BORRADOR,
    )

    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)

        if form.is_valid():
            form.save()

            return redirect(
                "actividades:panel_actividades_organizador"
            )
    else:
        form = ActividadForm(instance=actividad)

    return render(
        request,
        "actividades/formulario_actividad.html",
        {
            "form": form,
            "actividad": actividad,
        },
    )



main
