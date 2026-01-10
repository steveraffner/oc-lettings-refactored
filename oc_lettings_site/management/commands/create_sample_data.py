from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


class Command(BaseCommand):
    help = 'Create sample data for demonstration'

    def handle(self, *args, **kwargs):
        # Check if data already exists
        if Letting.objects.exists() or Profile.objects.exists():
            self.stdout.write(self.style.WARNING('Sample data already exists. Skipping.'))
            return

        self.stdout.write('Creating sample data...')

        # Create sample addresses
        address1 = Address.objects.create(
            number=7217,
            street='Bedford Street',
            city='Brunswick',
            state='GA',
            zip_code=31525,
            country_iso_code='USA'
        )

        address2 = Address.objects.create(
            number=4,
            street='Military Street',
            city='Willoughby',
            state='OH',
            zip_code=44094,
            country_iso_code='USA'
        )

        address3 = Address.objects.create(
            number=340,
            street='Wintergreen Avenue',
            city='Newport News',
            state='VA',
            zip_code=23601,
            country_iso_code='USA'
        )

        # Create sample lettings
        Letting.objects.create(title='Comfortable Apartment', address=address1)
        Letting.objects.create(title='Charming Cottage', address=address2)
        Letting.objects.create(title='Modern Studio', address=address3)

        # Create sample users and profiles
        user1 = User.objects.create_user(
            username='HeadlineGazer',
            email='headlinegazer@example.com',
            password='demo123'
        )
        Profile.objects.create(user=user1, favorite_city='Buenos Aires')

        user2 = User.objects.create_user(
            username='AirWow',
            email='airwow@example.com',
            password='demo123'
        )
        Profile.objects.create(user=user2, favorite_city='Barcelona')

        user3 = User.objects.create_user(
            username='TheBigCat',
            email='thebigcat@example.com',
            password='demo123'
        )
        Profile.objects.create(user=user3, favorite_city='Berlin')

        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
        self.stdout.write(f'- Created {Address.objects.count()} addresses')
        self.stdout.write(f'- Created {Letting.objects.count()} lettings')
        self.stdout.write(f'- Created {Profile.objects.count()} profiles')
