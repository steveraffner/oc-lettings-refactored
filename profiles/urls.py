"""
Configuration des URLs pour l'application profiles.

Ce module définit les routes URL pour afficher la liste des profils
et le détail d'un profil utilisateur.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
