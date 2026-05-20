from django.contrib import admin
from .models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'descricao', 'foto')

admin.site.register(Fotografia, ListandoFotografias)

