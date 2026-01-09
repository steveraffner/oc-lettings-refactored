"""
Configuration de l'interface d'administration pour l'application lettings.

Ce module enregistre les modèles Address et Letting dans l'admin Django.
"""

from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Configuration de l'administration pour le modèle Address."""

    list_display = ('number', 'street', 'city', 'state', 'zip_code', 'country_iso_code')
    search_fields = ('street', 'city')
    list_filter = ('state', 'city')


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """Configuration de l'administration pour le modèle Letting."""

    list_display = ('title', 'address')
    search_fields = ('title',)
