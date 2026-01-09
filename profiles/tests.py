"""Tests pour l'application profiles."""

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
class TestProfileModel:
    """Tests pour le modèle Profile."""

    def test_profile_creation(self):
        """Test la création d'un profil."""
        user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="Paris"
        )
        assert profile.user.username == "testuser"
        assert profile.favorite_city == "Paris"

    def test_profile_str(self):
        """Test la représentation en chaîne d'un profil."""
        user = User.objects.create_user(
            username="john",
            password="password123"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="London"
        )
        assert str(profile) == "john"

    def test_profile_without_favorite_city(self):
        """Test un profil sans ville favorite."""
        user = User.objects.create_user(
            username="alice",
            password="alicepass"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city=""
        )
        assert profile.favorite_city == ""
        assert str(profile) == "alice"


@pytest.mark.django_db
class TestProfilesViews:
    """Tests pour les vues profiles."""

    def test_profiles_index_view(self, client):
        """Test la vue index sans données."""
        url = reverse('profiles:index')
        response = client.get(url)
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_profiles_index_with_data(self, client):
        """Test la vue index avec données."""
        user = User.objects.create_user(
            username="bob",
            password="bobpass"
        )
        Profile.objects.create(
            user=user,
            favorite_city="Tokyo"
        )
        url = reverse('profiles:index')
        response = client.get(url)
        assert response.status_code == 200
        assert "bob" in response.content.decode()

    def test_profile_detail_view(self, client):
        """Test la vue de détail d'un profil."""
        user = User.objects.create_user(
            username="charlie",
            password="charliepass"
        )
        Profile.objects.create(
            user=user,
            favorite_city="New York"
        )
        url = reverse('profiles:profile', kwargs={'username': 'charlie'})
        response = client.get(url)
        assert response.status_code == 200
        assert "charlie" in response.content.decode()
        assert "New York" in response.content.decode()
