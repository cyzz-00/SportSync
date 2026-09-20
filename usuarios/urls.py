from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path(
        "registro/exitoso/",
        views.registro_exitoso,
        name="registro_exitoso",
    ),
]