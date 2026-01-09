"""Tests pour l'application principale OC Lettings."""


from django.urls import reverse


class TestHomePage:
    """Tests pour la page d'accueil."""

    def test_index_view(self, client):
        """Test de la vue index."""
        url = reverse('index')
        response = client.get(url)
        assert response.status_code == 200
        assert b'<title>Holiday Homes</title>' in response.content

    def test_index_content(self, client):
        """Test du contenu de la page d'accueil."""
        url = reverse('index')
        response = client.get(url)
        assert response.status_code == 200
        assert b'Welcome to Holiday Homes' in response.content
