from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "criado_em")
    search_fields = ("nome", "email", "mensagem")
    ordering = ("-criado_em",)
