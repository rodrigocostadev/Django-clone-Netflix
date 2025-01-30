
from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta      # <====== importando a classe Homepage do arquivo views, e adicionado a classe Detalhesfilme
from django.contrib.auth import views as auth_view
# from .views import homepage, homefilmes    # <====== Método anterior feito com function

app_name='filme'

urlpatterns = [
    # path('', homepage), <====== Método anterior feito com function
    # path('filmes/', homefilmes),  <====== Método anterior feito com function
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(),name='detalhesfilme'), # <========== entre <> foi passado o parametro pk (dev ser especificado o tipo de parametro. ex int, str ...), pk é Primary Key, ele serve para colocar um id no path de cada filme de maneira automática
    path('pesquisa/', Pesquisafilme.as_view(), name = 'pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'), 
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name='logout'), 
    path('editarperfil/', Paginaperfil.as_view(), name = 'editarperfil'),
    path('criarconta/', Criarconta.as_view(), name="criarconta")
]

