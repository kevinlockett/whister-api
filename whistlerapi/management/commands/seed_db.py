import random
import faker_commerce
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from whistlerapi.models import (AppUser)

class Command(BaseCommand):
    faker = Faker()
    faker.add_provider(faker_commerce.Provider)
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            '--user_count',
            help='Count of users to seed',
        )
    def handle(self, *args, **options):
        if options['user_count']:
            self.create_users(int(options['user_count']))
        else:
            self.create_users()
    def create_users(self, user_count=30):
        """
        Create random users
        """
        for _ in range(user_count):
            first_name = self.faker.first_name()
            last_name = self.faker.last_name()
            email = f'{first_name}.{last_name}@example.com'
            username = f'{first_name}{last_name[0]}{random.randint(100,500)}'
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password='password',
                is_active=True
            )
            Token.objects.create(
                user=user
            )
            AppUser.objects.create(
                authuser=user,
                role_id=random.randint(1,3),
                bio="",
                image="",
                address=self.faker.street_address(),
                city="Nashville",
                state_id=43,
                zipcode="37143",
                phone=self.faker.numerify('(###) ###-####'),
                shop_id=random.randint(1,4),
                skill_level_id=random.randint(1,4),
                music_style_id=random.randint(1,4),
                instrument_id="",
                approved=False
            )
