import os
import django
from django.conf import settings


def ensure_superuser_exists():
    """S'assure qu'un superutilisateur existe au démarrage de l'application"""
    if settings.configured:
        try:
            from django.contrib.auth.models import User

            # Vérifie s'il y a déjà un superutilisateur
            if not User.objects.filter(is_superuser=True).exists():
                username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
                email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@oc-lettings.com')
                password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Abc1234!')

                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                print(f"✅ Superuser '{username}' created successfully!")
            else:
                print("ℹ️ Superuser already exists")
        except Exception as e:
            print(f"⚠️ Could not create superuser: {e}")


# Exécuter au chargement du module
if os.environ.get('RUN_MAIN') != 'true':  # Éviter de s'exécuter deux fois en dev
    try:
        django.setup()
        ensure_superuser_exists()
    except Exception:
        pass  # Ignorer les erreurs si Django n'est pas encore prêt
