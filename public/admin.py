from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Projeto)
admin.site.register(Patrocinador)
admin.site.register(Topico)
admin.site.register(ApresentacaoEquipe)
@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido') # Colunas que aparecerão na lista
    list_filter = ('lido', 'data_envio') # Adiciona filtros na lateral
    search_fields = ('nome', 'email', 'mensagem') # Adiciona uma barra de busca
