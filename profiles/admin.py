"""
Configuration de l'interface d'administration pour l'application profiles.

Ce module enregistre le modèle Profile dans l'admin Django.
"""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configuration de l'administration pour le modèle Profile."""

    list_display = ('user', 'favorite_city')
    search_fields = ('user__username', 'favorite_city')
