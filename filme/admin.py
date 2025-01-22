from django.contrib import admin
from .models import Filme # o ponto de .models significa que estou importando da mesma pasta, no caso models.py esta na mesma pasta que admin.py

# Register your models here.
admin.site.register(Filme)