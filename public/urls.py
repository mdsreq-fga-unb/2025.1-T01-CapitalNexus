from . import views
from django.urls import path

urlpatterns = [
    path('sobre/', views.home, name='Sobre'),
]