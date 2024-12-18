from django.contrib import admin

from .models import Filme          # O .models "PONTO MODELS",  o PONTO vem de pegar o arquivo models que está na mesma pasta (ESSA LINHA FOI ADICIONADA MANUALMENTE)

# Register your models here.
admin.site.register(Filme)
