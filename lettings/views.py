"""
Vues pour l'application lettings.

Ce module contient les vues pour afficher la liste des locations
et le détail d'une location spécifique.
"""

from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Affiche la liste de toutes les locations disponibles.

    Args:
        request (HttpRequest): La requête HTTP

    Returns:
        HttpResponse: Page avec la liste des locations
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Args:
        request (HttpRequest): La requête HTTP
        letting_id (int): L'identifiant de la location

    Returns:
        HttpResponse: Page avec les détails de la location
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
