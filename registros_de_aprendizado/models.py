from django.db import models

class Topicos(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    texto = models.CharField(max_length=200)
    data_de_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.texto

class Entrada(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topico = models.ForeignKey(Topicos, on_delete=models.CASCADE) # Na vesão atual do django é obrigatório inserir o on_delete
    texto = models.TextField()
    data_de_adicao = models.DateTimeField(auto_now_add=True)

    class Meta: # Classe que ajuda a definir o plural de uma palavra
        verbose_name_plural = "entradas"

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        if len(self.texto) > 50:
            return self.texto[:50] + "..."
        else:
            return self.texto