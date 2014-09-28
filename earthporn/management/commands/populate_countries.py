from django.core.management.base import BaseCommand, CommandError
from earthporn.countries import countries
from earthporn.models import Country

class Command(BaseCommand):
    help = 'Populates countries model'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        for country in countries:
            c = Country(id=country)
            c.save()

        self.stdout.write('Successfully populated countries')