from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10] # <======== vai criar uma lista de filmes oredenada DE MANEIRA DECRESCENTE ( -data_criacao ) pela data de criação. 
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_emalta": lista_filmes}