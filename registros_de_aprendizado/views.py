from django.shortcuts import render
from .models import Topicos  # Seu model com T maiúsculo


def index(request):
    """Página inicial."""
    return render(request, "registros_de_aprendizado/index.html")


def topicos(request):
    """Mostra todos os tópicos."""
    topicos = Topicos.objects.order_by("data_de_adicao")
    contexto = {"topicos": topicos}
    return render(request, "registros_de_aprendizado/topicos.html", contexto)


def topico(request, topico_id):
    """Mostra um único tópico e suas entradas."""
    topico = Topicos.objects.get(id=topico_id)
    entradas = topico.entrada_set.order_by("-data_de_adicao")
    contexto = {"topico": topico, "entradas": entradas}
    return render(request, "registros_de_aprendizado/topico.html", contexto)