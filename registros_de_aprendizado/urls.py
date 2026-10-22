"""Define padrões de URL para registros de aprendizado."""

from django.urls import path
from . import views


app_name = "registros_de_aprendizado"

urlpatterns = [
    path('', views.index, name='index'), # Pagina inicial
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:topico_id>/', views.topico, name='topico') # Página de detalhes para um único assunto

]