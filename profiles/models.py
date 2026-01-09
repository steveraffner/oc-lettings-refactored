"""
Modèles de données pour l'application profiles.

Ce module contient le modèle Profile pour gérer
les profils utilisateurs.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil d'un utilisateur.

    Attributes:
        user (User): Utilisateur Django (relation OneToOne)
        favorite_city (str): Ville favorite de l'utilisateur (max 64 caractères)
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'

    def __str__(self):
        """
        Représentation textuelle du profil.

        Returns:
            str: Nom d'utilisateur du profil
        """
        return self.user.username
