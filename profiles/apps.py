"""Configuration de l'application profiles."""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration pour l'application profiles."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    verbose_name = 'Gestion des profils'
