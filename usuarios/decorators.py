from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def roles_permitidos(*roles):
    def decorador(vista):
        @wraps(vista)
        @login_required
        def verificar(request, *args, **kwargs):
            usuario = request.user

            if not usuario.is_active:
                raise PermissionDenied("Tu cuenta está desactivada.")

            if usuario.rol not in roles:
                raise PermissionDenied(
                    "No tienes permiso para acceder a esta página."
                )

            return vista(request, *args, **kwargs)

        return verificar

    return decorador