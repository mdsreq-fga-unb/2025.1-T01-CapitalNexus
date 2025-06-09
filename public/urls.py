from . import views
from django.urls import path

urlpatterns = [
    path('', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
]
