from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ["nome", "email", "mensagem"]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "placeholder": "Digite seu nome completo",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "seu.email@exemplo.com",
                    "autocomplete": "email",
                }
            ),
            "mensagem": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Escreva sua mensagem...",
                }
            ),
        }
