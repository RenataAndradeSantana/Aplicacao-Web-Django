from django.shortcuts import render, redirect
from .models import Topicos, Entrada  # Seu model com T maiúsculo
from .forms import TopicoForm, EntradaForm

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

def novo_topico(request):
    """Adiciona um novo tópico"""
    if request.method != "POST": 
        form = TopicoForm() # Requisição GET: exibe um formulário em branco
    else:
        form = TopicoForm(data=request.POST) # Passa os dados para o formulário
        if form.is_valid():
            form.save()
            return redirect("registros_de_aprendizado:topicos")

    contexto = {"form": form}
    return render(
        request, "registros_de_aprendizado/novo_topico.html", contexto
    )

def nova_entrada(request, topico_id):
    """Adiciona uma nova anotação vinculada a um tópico específico."""
    topico = Topicos.objects.get(id=topico_id)

    if request.method != "POST":
        form = EntradaForm()
    else:
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.topico = topico
            nova_entrada.save()
            return redirect(
                "registros_de_aprendizado:topico", topico_id=topico.id
            )
    contexto = {"topico": topico, "form": form}
    return render(
        request, "registros_de_aprendizado/nova_entrada.html", contexto
    )

def edita_entrada(request, entrada_id):
    """Edita uma anotação existente no banco de dados."""
    entrada = Entrada.objects.get(id=entrada_id) 
    topico = entrada.topico

    if request.method != "POST":
        form = EntradaForm(instance=entrada)
    else:
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("registros_de_aprendizado:topico", topico_id=topico.id
            )
    contexto = {"entrada": entrada, "topico":topico, "form":form}
    return render(
        request, "registros_de_aprendizado/edita_entrada.html", contexto
    )

def deleta_topico(request, topico_id):
    """Exclui um tópico e todas as suas entradas associadas."""
    topico = Topicos.objects.get(id=topico_id)
    if request.method == "POST":
        topico.delete()
    return redirect("registros_de_aprendizado:topicos")


def deleta_entrada(request, entrada_id):
    """Exclui uma entrada específica."""
    entrada = Entrada.objects.get(id=entrada_id)
    topico_id = entrada.topico.id
    if request.method == "POST":
        entrada.delete()
    return redirect("registros_de_aprendizado:topico", topico_id=topico_id)