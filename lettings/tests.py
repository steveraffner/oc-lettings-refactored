"""Tests pour l'application lettings."""

import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    """Tests pour le modèle Address."""

    def test_address_creation(self):
        """Test la création d'une adresse."""
        address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="USA"
        )
        assert address.number == 123
        assert address.city == "Test City"

    def test_address_str(self):
        """Test la représentation en chaîne d'une adresse."""
        address = Address.objects.create(
            number=456,
            street="Main St",
            city="Springfield",
            state="IL",
            zip_code=62701,
            country_iso_code="USA"
        )
        assert str(address) == "456 Main St"


@pytest.mark.django_db
class TestLettingModel:
    """Tests pour le modèle Letting."""

    def test_letting_creation(self):
        """Test la création d'un letting."""
        address = Address.objects.create(
            number=789,
            street="Oak Ave",
            city="Portland",
            state="OR",
            zip_code=97201,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="Cozy Apartment",
            address=address
        )
        assert letting.title == "Cozy Apartment"
        assert letting.address == address

    def test_letting_str(self):
        """Test la représentation en chaîne d'un letting."""
        address = Address.objects.create(
            number=321,
            street="Elm St",
            city="Seattle",
            state="WA",
            zip_code=98101,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="Modern Studio",
            address=address
        )
        assert str(letting) == "Modern Studio"


@pytest.mark.django_db
class TestLettingsViews:
    """Tests pour les vues lettings."""

    def test_lettings_index_view(self, client):
        """Test la vue index sans données."""
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_lettings_index_with_data(self, client):
        """Test la vue index avec données."""
        address = Address.objects.create(
            number=100,
            street="Test St",
            city="Testville",
            state="TV",
            zip_code=10000,
            country_iso_code="USA"
        )
        Letting.objects.create(  # noqa: F841
            title="Test Letting",
            address=address
        )
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200
        assert "Test Letting" in response.content.decode()

    def test_letting_detail_view(self, client):
        """Test la vue de détail d'un letting."""
        address = Address.objects.create(
            number=200,
            street="Detail St",
            city="Detailtown",
            state="DT",
            zip_code=20000,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="Detail Letting",
            address=address
        )
        url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = client.get(url)
        assert response.status_code == 200
        assert "Detail Letting" in response.content.decode()
        assert "200 Detail St" in response.content.decode()
