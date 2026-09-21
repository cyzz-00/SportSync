from django.contrib import admin
main
from .models import Actividad

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'deporte', 'estado', 'organizador')
    list_filter = ('estado', 'deporte', 'fecha')
    search_fields = ('nombre', 'descripcion')
    ordering = ('fecha', 'hora')


# Register your models here.
main
