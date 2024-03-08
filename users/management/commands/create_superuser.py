from django.core.management import BaseCommand

from users.models import User
from config.settings import SUPERUSER_PASSWORD, SUPERUSER_EMAIL


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=SUPERUSER_EMAIL,
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(SUPERUSER_PASSWORD)
        user.save()
