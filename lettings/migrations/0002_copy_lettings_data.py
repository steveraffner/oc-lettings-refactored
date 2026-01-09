"""
Migration personnalisée pour copier les données de Letting et Address.

Cette migration copie les locations et adresses de oc_lettings_site vers lettings.
"""

from django.db import migrations


def copy_lettings_data(apps, schema_editor):
    """Copie les addresses et lettings de l'ancienne app vers la nouvelle."""
    try:
        # Copier les addresses d'abord
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
        NewAddress = apps.get_model('lettings', 'Address')
        
        for old_address in OldAddress.objects.all():
            NewAddress.objects.create(
                id=old_address.id,
                number=old_address.number,
                street=old_address.street,
                city=old_address.city,
                state=old_address.state,
                zip_code=old_address.zip_code,
                country_iso_code=old_address.country_iso_code
            )
        
        # Copier les lettings ensuite
        OldLetting = apps.get_model('oc_lettings_site', 'Letting')
        NewLetting = apps.get_model('lettings', 'Letting')
        
        for old_letting in OldLetting.objects.all():
            new_address = NewAddress.objects.get(id=old_letting.address.id)
            NewLetting.objects.create(
                id=old_letting.id,
                title=old_letting.title,
                address=new_address
            )
    except LookupError:
        # L'ancienne app n'existe pas (ex: test database)
        pass


def reverse_copy_lettings_data(apps, schema_editor):
    """Supprime les données de la nouvelle app (rollback)."""
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    
    NewLetting.objects.all().delete()
    NewAddress.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0002_alter_address_options_alter_profile_options_and_more"),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data, reverse_copy_lettings_data),
    ]
