from . import views
from django.urls import path

app_name='membros'

urlpatterns = [
    path('', views.home, name='home'),
    path('reunioes/', views.pagina_reunioes, name='reunioes'),
    path('reunioes/marcar/', views.marcar_reuniao, name='marcar-reuniao'),
    path('reunioes/<int:reuniao_id>/editar/', views.editar_reuniao, name='editar-reuniao'),
    path('reunioes/<int:reuniao_id>/chamada/', views.fazer_chamada, name='chamada'),
    path('presencas/', views.pagina_faltas_advertencias, name='faltaseadvertencias'),
    path('presencas/<int:falta_id>/justificar/', views.justificar_falta, name='justificar-falta'),
    path('presencas/justificativas/', views.pagina_avaliar_justificativas, name='justificativas'),
    path('presencas/justificativas/<int:just_id>/processar/', views.processar_justificativa, name='processar'),
    path('presencas/advertencias/', views.pagina_gerenciar_advertencias, name='advertencias'),
    path('presencas/advertencias/registrar', views.registrar_advertencia, name='criar-advertencia'),
    path('advertencias/<int:advertencia_id>/editar/', views.editar_advertencia, name='editar-advertencia'),
    path('advertencias/<int:advertencia_id>/excluir/', views.excluir_advertencia, name='excluir-advertencia'),
    path('materiais/', views.pagina_lista_de_materiais, name='materiais'),
    path('materiais/novo/', views.novo_material, name='novo-material'),
    path('materiais/<int:material_id>/editar/', views.editar_material, name='editar-material'),
    path('api/material/<int:material_id>/', views.material_detalhes_api, name='api-material-detalhes'),
    path('materiais/<int:material_id>/reservar/', views.reservar_material, name='reservar-material'),
    path('materiais/<int:material_id>/devolver/', views.devolver_material, name='devolver-material'),
    path('materiais/<int:material_id>/marcar-disponivel/', views.marcar_material_disponivel, name='marcar-material-disponivel'),
    path('materiais/solicitar/', views.solicitar_material, name='solicitar-material'),
    path('membros/', views.pagina_lista_membros, name='membros'),
    path('membros/novo/', views.membro_novo, name='membro-novo'),
    path('membros/<str:matricula>/editar/', views.membro_editar, name='editar-membro'),
    path('membros/<str:matricula>/excluir/', views.membro_excluir, name='excluir-membro'),
    path('painel/', views.pagina_painel_administrativo, name='painel'),
    path('painel/nucleo/<str:pk>/editar/', views.nucleo_editar, name='editar-nucleo'),
    path('api/mensagens/<int:mensagem_id>/marcar-lida/', views.marcar_mensagem_lida, name='marcar-mensagem-lida'),
]
