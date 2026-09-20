from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# MODELO DE USUARIO PERSONALIZADO 
# Se crea un modelo de usuario personalizado para utilizar el correo electrónico como identificador único en lugar del nombre de usuario.
class UsuarioManager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.get(email__iexact=email.strip())

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio.")

        email = self.normalize_email(email.strip()).lower()
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("rol", self.model.Rol.ADMINISTRADOR)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El administrador debe tener is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El administrador debe tener is_superuser=True.")

        if extra_fields.get("rol") != self.model.Rol.ADMINISTRADOR:
            raise ValueError("El superusuario debe tener rol Administrador.")

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractUser):

    class Rol(models.TextChoices):
        PARTICIPANTE = "participante", "Participante"
        ORGANIZADOR = "organizador", "Organizador"
        ADMINISTRADOR = "administrador", "Administrador"

    rol = models.CharField(
        "rol",
        max_length=20,
        choices=Rol.choices,
        default=Rol.PARTICIPANTE,
    )

    username = None
    email = models.EmailField("correo electrónico", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    def save(self, *args, **kwargs):
        self.email = self.email.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email