from django import forms
from .models import Topicos, Entrada


class TopicoForm(forms.ModelForm):
    """Formulário para adicionar novos tópicos de estudo"""

    class Meta: # Configura o comportamento ea ligação do form com o banco 
        model = Topicos
        fields = ["texto"]
        labels = {"texto":""}

class EntradaForm(forms.ModelForm):
    """Formulário para acicionar ou editar anotações."""

    class Meta:
        model = Entrada
        fields = ["texto"]
        labels = {"texto": "Sua anotação:"}
        widgets = {
            "texto": forms.Textarea(
                attrs={
                    "cols": 80,
                    "rows": 5,
                    "placeholder": "Digite os detalhes do que aprendeu..."
                }
            )
        }