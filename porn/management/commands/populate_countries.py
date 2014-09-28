from django.core.management.base import BaseCommand, CommandError
from porn.countries import countries
from porn.models import Country

class Command(BaseCommand):
    help = 'Populates countries model'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        for country in countries:
            c = Country(country=country)
            c.save()

        self.stdout.write('Successfully populated countries')