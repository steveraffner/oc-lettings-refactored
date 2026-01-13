from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import migrations
import os


def create_default_superuser(apps, schema_editor):
    """Crée un superutilisateur par défaut s'il n'existe pas"""
    if not User.objects.filter(is_superuser=True).exists():
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@oc-lettings.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Abc1234!')
        
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )


class Migration(migrations.Migration):
    dependencies = [
        ('oc_lettings_site', '0003_remove_letting_address_remove_profile_user_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_default_superuser, migrations.RunPython.noop),
    ]