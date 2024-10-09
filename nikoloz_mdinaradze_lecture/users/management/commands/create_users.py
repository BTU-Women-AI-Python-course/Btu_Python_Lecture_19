from django.contrib.auth.models import User
from django.core.management import BaseCommand
from uuid import uuid4

from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create a specific number of users"

    def add_arguments(self, parser):
        parser.add_argument(
            'numbers_of_users',
            nargs="?",
            type=int,
            help="The number of users to create",
            default=20
        )

    def handle(self, *args, **options):
        number = options['numbers_of_users']
        for i in range(number):
            username = f'user_{uuid4().hex}'
            email = f'{username}@example.com'
            password = get_random_string(8)

            User.objects.create_user(username=username, email=email, password=password)
            print(f"user {username} has created")

        print("Done")
