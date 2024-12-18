from django.db import models
from django.utils import timezone

# Create your models here.


LISTA_CATEGORIAS = (
    ("ANALISES","Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO","Apresentação"),
    ("OUTROS","Outros"),
)

# Criar o filme

# A classe filme é uma subclasse, por isso por padrão ela recebe no parenteses (models.Model)
class Filme(models.Model): # NA TELA DE ADMIN O NOME DA CLASSE FILME VAI FICAR NO PLURAL ( S )
    titulo = models.CharField(max_length=100)  # CHARFIELD É UM PEQUENO CAMPO DE TEXTO, foi definido o maxlength para limitar o numero de caracteres
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000) # TEXTFIELD É UM CAMPO DE TEXTO MAIOR, foi definido o maxlength para limitar o numero de caracteres
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS) # É um charfield, mas é atraves de opções da lista de categorias. CHOICES = OPÇÕES
    visualizacoes = models.IntegerField(default=0) # INTEGERFIELD É UM VALOR NUMÉRICO
    data_criacao = models.DateTimeField(default=timezone.now)
    
    # Essa função diz para cada classe do python o que vai aparecer quando o usuário solicitar um print em algum item dessa classe
    def __str__(self):
        # Essa função muda o nome de Filme object (1) para o nome que voce definir
        return self.titulo  #retorna o titulo do filme

# Criar os episodios