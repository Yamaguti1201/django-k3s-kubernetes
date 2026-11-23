from django.urls import path
from . import views

app_name = "contatos"

urlpatterns = [
    path("", views.cadastro, name="cadastro"),
    path("registros/", views.lista, name="lista"),
    path("health/", views.health, name="health"),
]
