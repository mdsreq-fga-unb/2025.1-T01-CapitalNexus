from . import views
from django.urls import path

urlpatterns = [
    path('', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('projetos/', views.pagina_projetos, name='pagina-projetos'),
]
