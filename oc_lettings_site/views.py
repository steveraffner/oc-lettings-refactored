"""
Vues pour l'application principale OC Lettings.

Ce module contient la vue de la page d'accueil du site.
"""

from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site OC Lettings.

    Args:
        request (HttpRequest): La requête HTTP

    Returns:
        HttpResponse: Page d'accueil rendue
    """
    return render(request, 'index.html')
