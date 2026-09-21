from django.contrib import admin
from django.urls import path, include

urlpatterns = [
main
    path('admin/', admin.site.urls),
    path('', include('core.urls')),       # Páginas estáticas
    path('usuarios/', include('usuarios.urls')), # <-- Esta línea es crucial
    path('actividades/', include('actividades.urls')),

    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("acerca/", acerca, name="acerca"),
    # agregar las rutas de la aplicación usuarios
    path("usuarios/", include("usuarios.urls")),
    # agregar las rutas de la aplicación actividades
    path("actividades/", include("actividades.urls")),

main
]