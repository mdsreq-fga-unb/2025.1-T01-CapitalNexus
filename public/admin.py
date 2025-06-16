from django.contrib import admin
from .models import Projeto, MensagemContato
# Register your models here.

admin.site.register(Projeto)
@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido') # Colunas que aparecerão na lista
    list_filter = ('lido', 'data_envio') # Adiciona filtros na lateral
    search_fields = ('nome', 'email', 'mensagem') # Adiciona uma barra de busca
