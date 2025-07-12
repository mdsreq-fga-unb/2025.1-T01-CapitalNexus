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
]
