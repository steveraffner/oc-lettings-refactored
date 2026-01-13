from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create superuser from environment variables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force recreation of superuser if exists',
        )

    def handle(self, *args, **kwargs):
        force = kwargs.get('force', False)
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Abc1234!')

        self.stdout.write(f'Creating superuser with username: {username}')
        self.stdout.write(f'Email: {email}')
        self.stdout.write(f'Force recreation: {force}')

        existing_user = User.objects.filter(username=username).first()

        if force and existing_user:
            existing_user.delete()
            self.stdout.write(self.style.WARNING(f'Deleted existing user "{username}"'))
            existing_user = None

        if not existing_user:
            try:
                user = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Superuser "{username}" created successfully.')
                )
                self.stdout.write(
                    f'User ID: {user.id}, is_staff: {user.is_staff}, '
                    f'is_superuser: {user.is_superuser}'
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to create superuser: {e}')
                )
                raise
        else:
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists.')
            )
            self.stdout.write(
                f'Existing user ID: {existing_user.id}, is_staff: {existing_user.is_staff}, '
                f'is_superuser: {existing_user.is_superuser}'
            )
