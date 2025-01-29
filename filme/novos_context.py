from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8] # <======== vai criar uma lista de filmes oredenada DE MANEIRA DECRESCENTE ( -data_criacao ) pela data de criação. 
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque" : filme_destaque}
    # return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}


# def filme_destaque(request):
#     filme = Filme.objects.order_by('-data-criacao')[0]
#     return {"filme_destaque" : filme}