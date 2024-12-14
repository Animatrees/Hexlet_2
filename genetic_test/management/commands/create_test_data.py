import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from genetic_test.models import GeneticTest
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates test data for GeneticTest'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test', email='admin@example.com')
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created.'))

        animal_names = ['Белла', 'Дуня', 'Луна', 'Молли', 'Люся', 'Маруся']
        species = ['корова', 'коза', 'овца']
        health_status_choices = ['good', 'poor']

        test_data = []
        for _ in range(10):
            test_date = datetime.now().date() - timedelta(days=random.randint(0, 365))
            test_data.append(
                GeneticTest(
                    animal_name=random.choice(animal_names),
                    species=random.choice(species),
                    test_date=test_date,
                    milk_yield=round(random.uniform(5.0, 50.0), 2),
                    health_status=random.choice(health_status_choices),
                )
            )

        GeneticTest.objects.bulk_create(test_data)
        self.stdout.write(self.style.SUCCESS(f'Created {len(test_data)} genetic tests.'))
