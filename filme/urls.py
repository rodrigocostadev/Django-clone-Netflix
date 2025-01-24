
from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme      # <====== importando a classe Homepage do arquivo views, e adicionado a classe Detalhesfilme
# from .views import homepage, homefilmes    # <====== Método anterior feito com function

app_name='filme'

urlpatterns = [
    # path('', homepage), <====== Método anterior feito com function
    # path('filmes/', homefilmes),  <====== Método anterior feito com function
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(),name='detalhesfilme'), # <========== entre <> foi passado o parametro pk (dev ser especificado o tipo de parametro. ex int, str ...), pk é Primary Key, ele serve para colocar um id no path de cada filme de maneira automática
]

