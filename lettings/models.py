"""
Modèles de données pour l'application lettings.

Ce module contient les modèles Address et Letting pour gérer
les informations des locations immobilières.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse physique.

    Attributes:
        number (int): Numéro de rue (max 9999)
        street (str): Nom de la rue (max 64 caractères)
        city (str): Nom de la ville (max 64 caractères)
        state (str): Code de l'état (2 caractères)
        zip_code (int): Code postal (max 99999)
        country_iso_code (str): Code ISO du pays (3 caractères)
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        """
        Représentation textuelle de l'adresse.

        Returns:
            str: Numéro et nom de rue
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location immobilière.

    Attributes:
        title (str): Titre de la location (max 256 caractères)
        address (Address): Adresse de la location (relation OneToOne)
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """
        Représentation textuelle de la location.

        Returns:
            str: Titre de la location
        """
        return self.title
