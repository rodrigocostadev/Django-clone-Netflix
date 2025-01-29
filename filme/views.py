from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin # <====== LoginRequiredMixin é uma classe em python que eu passo para as CBV

# criar: url - view - html

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"
    
    
class Homefilmes(LoginRequiredMixin,ListView):  # <========= o objetivo dessa classe é exibir uma lista de filmes (uma lista de objetos no banco de dados) 
# então quando vc tem uma view cujo objetivo é exibir uma lista de itens do seu banco de dados vc pode importar de uma listView
# Uma list View  espera que voce passe 2 informações, o template_name e o modelo
    template_name = "homefilmes.html"
    model =  Filme    # <======== model é o modelo do banco de dados que eu vou pegar a minha lista. 
    # Com o uso do listview e do model ele vai me retornar uma object_list, esse object_list eu devo passar para o html da pagina especifica, no caso "Homefilmes"


#  vai criar uma pagina para cada filme
class Detalhesfilme(LoginRequiredMixin,DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # no listview ele retornava uma lista,  e a variavel digamos a ser renderizada no html era object_list
    # no detailview, a variavel a ser renderizada no html será o object (apenas 1 item)
    
    # a função get vai retornar ao usuário o link que ela está querendo acessar
    def get(self,request,*args,**kwargs): # <====== por padrão o get recebe esses 4 argumentos
    
        # descobrir qual filme ele está acessando:
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()   # <===== salva a modificação no banco de dados
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(Detalhesfilme, self).get(request, *args, **kwargs) # redireciona o usuário para a url final
    
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria)[0:5]  # <====== essa linha está pegando os objects da classe Filmes, no caso pegando 5 filmes cuja categoria são relacionadas com o filme escolhido
        context['filmes_relacionados'] = filmes_relacionados
        return context

class Pesquisafilme(LoginRequiredMixin,ListView):
    template_name = "pesquisa.html"
    model = Filme
    
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__contains=termo_pesquisa)
            return object_list
        else:
            return None







# def homepage(request):
#     return render(request, "homepage.html")  # <============ precisa ser passado 2 parametros, 1 - REQUEST, 2 - NOME DO TEMPLATE

# def homefilmes(request):
#     context = {}                                       # <============ context é um dicionário python
#     lista_filmes = Filme.objects.all()                 # <============ PEGANDO INFORMAÇÕES DO BANCO DE DADOS 
#     context['lista_filmes'] = lista_filmes             # <============ criei uma chave lista_filmes e estou atribuindo valor a essa chave
#     return render(request, "homefilmes.html", context) # <============ Na função render posso passar um novo parametro, que é o context



    