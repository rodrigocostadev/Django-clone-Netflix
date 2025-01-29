from django.contrib import admin
from .models import Filme, Episodio, Usuario # o ponto de .models significa que estou importando da mesma pasta, no caso models.py esta na mesma pasta que admin.py
from django.contrib.auth.admin import UserAdmin

# Só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(("Histórico", {'fields':('filmes_vistos', )}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

# Configurando os campos do user admin:  (TUPLA)
# Primeira informação = NOME DA SEÇÃO/ CHAVE DO DICIONÁRIO = FIELDS  : ( NOME DO PRIMEIRO CAMPO, NOME DO SEGUNDO CAMPO ... )
# [
#     ("Informações pessoais", {'fields':('Primeiro nome', 'Último nome')})
# ]




