import praw
import dstk
import re
from django.core.management.base import BaseCommand, CommandError
from earthporn.models import Place, Country
from urllib import urlopen

class Command(BaseCommand):
    help = 'Fetches new images from /r/earthporn'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.r = praw.Reddit('user-agent')
        self.sub = self.r.get_subreddit('earthporn')
        self.dstk = dstk.DSTK()

    def handle(self, *args, **options):
        pattern = re.compile("[\w\s']+|[.,!?;]")
        count = 0
        for post in self.sub.get_new(limit=500):
            if self.contains(post.url) or self.invalid_image(post.url):
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
                count += 1

        self.stdout.write('Successfully fetched {} new images'.format(count))

    def invalid_image(self, image):
        return 'image' not in urlopen(image).info().type

    # TODO: Remove hack.
    def get_country(self, coords):
        politics = self.dstk.coordinates2politics(coords)
        if politics[0]['politics'] == None:
            return None
        for type in politics[0]['politics']:
            if type['friendly_type'] == 'country':
                name = type['name']
                if name == 'England' or name == 'Scotland' or name == 'Wales':
                    name = 'United Kingdom'
                elif name == 'Iran (Islamic Republic of)':
                    name = 'Iran, Islamic Republic of'
                elif name == 'United Republic of Tanzania':
                    name = 'Tanzania, United Republic of'
                elif name == 'Taiwan':
                    name = 'Taiwan, Province of China'
                return Country.objects.get(id=name)
        return None

    def contains(self, image):
        return Place.objects.filter(image=image).count() > 0
