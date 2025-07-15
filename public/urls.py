from . import views
from django.urls import path

app_name='publico'

urlpatterns = [
    path('', views.sobre, name='sobre'),
    path('contato/', views.pagina_contato, name='contato'),
    path('projetos/', views.pagina_projetos, name='projetos'),
]
