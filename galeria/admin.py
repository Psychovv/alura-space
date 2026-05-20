from django.contrib import admin
from .models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'descricao', 'foto')
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)

