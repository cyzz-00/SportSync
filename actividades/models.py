main
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Actividad(models.Model):
    
    # Definición de estados posibles (CR-19)
    class Estado(models.TextChoices):
        BORRADOR = 'borrador', 'Borrador'
        PUBLICADA = 'publicada', 'Publicada'
        INSCRIPCION_CERRADA = 'inscripcion_cerrada', 'Inscripción Cerrada'
        EN_CURSO = 'en_curso', 'En Curso'
        FINALIZADA = 'finalizada', 'Finalizada'
        CANCELADA = 'cancelada', 'Cancelada'

    # Campos básicos de la actividad
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la actividad")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    deporte = models.CharField(max_length=100)
    fecha = models.DateField(verbose_name="Fecha del evento")
    hora = models.TimeField(verbose_name="Hora de inicio")
    lugar = models.CharField(max_length=200, verbose_name="Lugar o dirección")
    
    # Control de cupo (Punto 7 de Fase 5)
    cupo_maximo = models.PositiveIntegerField(
        verbose_name="Cupo máximo",
        help_text="Número máximo de participantes permitidos."
    )
    
    costo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        verbose_name="Costo de inscripción"
    )
    
    # Estado actual (CR-19)

from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Actividad(models.Model):



    class Tipo(models.TextChoices):
        ACTIVIDAD = "actividad", "Actividad deportiva"
        TORNEO = "torneo", "Torneo individual"












    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        PUBLICADA = "publicada", "Publicada"
        INSCRIPCION_CERRADA = "inscripcion_cerrada", "Inscripción cerrada"
        EN_CURSO = "en_curso", "En curso"
        FINALIZADA = "finalizada", "Finalizada"
        CANCELADA = "cancelada", "Cancelada"

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField("descripción", max_length=3000)

    tipo = models.CharField(
        max_length=20,
        choices=Tipo.choices,
        default=Tipo.ACTIVIDAD,
    )

    deporte = models.CharField(max_length=100)
    ubicacion = models.CharField("ubicación", max_length=250)

    fecha_inicio = models.DateTimeField("fecha y hora de inicio")
    fecha_fin = models.DateTimeField("fecha y hora de finalización")

    cupo_maximo = models.PositiveIntegerField(
        "cupo máximo",
        validators=[MinValueValidator(1)],
    )

    costo = models.DecimalField(
        "costo de inscripción",
        max_digits=8,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    organizador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="actividades_organizadas",
    )

main
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.BORRADOR,
main
        verbose_name="Estado actual"
    )
    
    # Relación con el usuario organizador
    organizador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='actividades_organizadas',
        limit_choices_to={'rol': 'organizador'}, # Solo muestra usuarios con rol organizador
        verbose_name="Organizador"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"

    def clean(self):
        # Validación de regla de negocio: El cupo no puede ser cero o negativo
        if self.cupo_maximo <= 0:
            raise ValidationError("El cupo máximo debe ser un número mayor a cero.")
        super().clean()

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['fecha', 'hora']

    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)














    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cupo_maximo__gte=1),
                name="actividad_cupo_mayor_cero",
            ),
            models.CheckConstraint(
                condition=models.Q(costo__gte=0),
                name="actividad_costo_no_negativo",
            ),
            models.CheckConstraint(
                condition=models.Q(fecha_fin__gt=models.F("fecha_inicio")),
                name="actividad_fin_posterior_inicio",
            ),
        ]

    def clean(self):
        super().clean()

        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_fin <= self.fecha_inicio:
                raise ValidationError({
                    "fecha_fin": (
                        "La finalización debe ser posterior al inicio."
                    ),
                })

    def __str__(self):
        return self.nombre
main
