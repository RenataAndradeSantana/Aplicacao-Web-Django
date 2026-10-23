"""Define padrões de URL para registros de aprendizado."""

from django.urls import path
from . import views


app_name = "registros_de_aprendizado"

urlpatterns = [
    path('', views.index, name='index'), # Pagina inicial
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:topico_id>/', views.topico, name='topico'), # Página de detalhes para um único assunto
    path('novo_topico/', views.novo_topico, name="novo_topico"),
    path('nova_entrada/<int:topico_id>/', views.nova_entrada, name="nova_entrada"),
    path('edita_entrada/<int:entrada_id>/', views.edita_entrada, name="edita_entrada"),
    path('deleta_topico/<int:topico_id>/', views.deleta_topico, name="deleta_topico"),
    path('deleta_entrada/<int:entrada_id>/', views.deleta_entrada, name="deleta_entrada"),

]