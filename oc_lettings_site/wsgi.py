import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()

# Créer le superutilisateur si nécessaire
try:
    from .startup import ensure_superuser_exists
    ensure_superuser_exists()
except Exception as e:
    print(f"Startup hook error: {e}")
