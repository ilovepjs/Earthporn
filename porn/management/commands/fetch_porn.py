import praw
import dstk
import re
from django.core.management.base import BaseCommand, CommandError
from porn.models import Place, Country


class Command(BaseCommand):
    help = 'Fetches new images from /r/earthporn'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.r = praw.Reddit('user-agent')
        self.sub = self.r.get_subreddit('earthporn')
        self.dstk = dstk.DSTK()

    def handle(self, *args, **options):
        pattern = re.compile("[\w\s']+|[.,!?;]")
        for post in self.sub.get_new():
            if self.contains(post.url):
                continue
            title = post.title.encode('ascii', 'ignore')
            place = self.dstk.text2places(title)
            if place != []:
                name = pattern.search(title).group()
                lat = place[0]['latitude']
                lon = place[0]['longitude']

                country = self.get_country((float(lat), float(lon)))
                if country is None:
                    continue
                p = Place(image=post.url, name=name, caption=title, latitude=lat, longitude=lon, country=country)
                p.save()

        self.stdout.write('Successfully fetched new images')

    def get_country(self, coords):
        politics = self.dstk.coordinates2politics(coords)
        for type in politics[0]['politics']:
            if type['friendly_type'] == 'country':
                name = type['name']
                # TODO: Remove hack.
                if name == 'England':
                    name = 'United Kingdom'
                return Country.objects.get(country=name)
        return None

    def contains(self, image):
        return Place.objects.filter(image=image).count() > 0
