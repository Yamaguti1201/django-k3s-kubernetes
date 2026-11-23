from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import ContatoForm
from .models import Contato


def cadastro(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            messages.success(
                request,
                f"Registro de {contato.nome} salvo com sucesso no MySQL!",
            )
            return redirect("contatos:lista")
    else:
        form = ContatoForm()

    total_registros = Contato.objects.count()
    return render(
        request,
        "contatos/cadastro.html",
        {
            "form": form,
            "total_registros": total_registros,
        },
    )


def lista(request):
    contatos = Contato.objects.all()
    return render(
        request,
        "contatos/lista.html",
        {
            "contatos": contatos,
            "total_registros": contatos.count(),
        },
    )


def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return JsonResponse({"status": "ok", "database": "connected"})
    except Exception as exc:
        return JsonResponse(
            {"status": "error", "database": str(exc)},
            status=503,
        )
