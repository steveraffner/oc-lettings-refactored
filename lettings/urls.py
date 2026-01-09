"""
Configuration des URLs pour l'application lettings.

Ce module définit les routes URL pour afficher la liste des locations
et le détail d'une location.
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
