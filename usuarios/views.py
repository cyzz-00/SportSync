from django.shortcuts import render, redirect

from .forms import RegistroForm


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