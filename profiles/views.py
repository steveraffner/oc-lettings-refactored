"""
Vues pour l'application profiles.

Ce module contient les vues pour afficher la liste des profils
et le détail d'un profil spécifique.
"""

from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Affiche la liste de tous les profils utilisateurs.

    Args:
        request (HttpRequest): La requête HTTP

    Returns:
        HttpResponse: Page avec la liste des profils
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche les détails d'un profil utilisateur spécifique.

    Args:
        request (HttpRequest): La requête HTTP
        username (str): Le nom d'utilisateur

    Returns:
        HttpResponse: Page avec les détails du profil
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
