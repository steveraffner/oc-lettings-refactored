"""Configuration de l'application lettings."""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration pour l'application lettings."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
    verbose_name = 'Gestion des locations'
