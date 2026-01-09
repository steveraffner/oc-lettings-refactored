"""
Migration personnalisée pour copier les données de Profile.

Cette migration copie les profils de oc_lettings_site vers profiles.
"""

from django.db import migrations


def copy_profiles(apps, schema_editor):
    """Copie les profils de l'ancienne app vers la nouvelle."""
    try:
        OldProfile = apps.get_model('oc_lettings_site', 'Profile')
        NewProfile = apps.get_model('profiles', 'Profile')
        
        for old_profile in OldProfile.objects.all():
            NewProfile.objects.create(
                id=old_profile.id,
                user=old_profile.user,
                favorite_city=old_profile.favorite_city
            )
    except LookupError:
        # L'ancienne app n'existe pas (ex: test database)
        pass


def reverse_copy_profiles(apps, schema_editor):
    """Supprime les profils de la nouvelle app (rollback)."""
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0002_alter_address_options_alter_profile_options_and_more"),
    ]

    operations = [
        migrations.RunPython(copy_profiles, reverse_copy_profiles),
    ]
