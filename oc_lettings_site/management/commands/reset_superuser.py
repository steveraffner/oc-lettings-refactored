from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Reset all users and create fresh superuser'

    def handle(self, *args, **kwargs):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Abc1234!')

        self.stdout.write('🗑️ Deleting all existing users...')
        user_count = User.objects.count()
        User.objects.all().delete()
        self.stdout.write(f'Deleted {user_count} users')

        self.stdout.write(f'👤 Creating fresh superuser: {username}')
        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superuser "{username}" created successfully!')
            )
            self.stdout.write(f'User ID: {user.id}')
            self.stdout.write(f'Staff: {user.is_staff}')
            self.stdout.write(f'Superuser: {user.is_superuser}')
            self.stdout.write(f'Active: {user.is_active}')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Failed to create superuser: {e}')
            )
            raise
