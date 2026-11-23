from django.db import models


class Contato(models.Model):
    nome = models.CharField("Nome", max_length=120)
    email = models.EmailField("E-mail", max_length=180)
    mensagem = models.TextField("Mensagem")
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["-criado_em", "-id"]
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.nome} <{self.email}>"
