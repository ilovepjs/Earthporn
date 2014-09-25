import praw
import dstk
import re
from django.core.management.base import BaseCommand, CommandError
from porn.models import Place

class Command(BaseCommand):
	help = 'Fetches new images from /r/earthporn'

	def __init__(self, *args, **kwargs):
		super(Command, self).__init__(*args, **kwargs)
		self.r = praw.Reddit('user-agent')		
		self.sub = self.r.get_subreddit('earthporn') 
		self.dstk = dstk.DSTK()

	def handle(self, *args, **options):
		count = 0
		pattern = re.compile("[\w\s']+|[.,!?;]")
		for post in self.sub.get_hot():
			if count >= 15:
				break
			if self.contains(post.url):
				continue
			title = post.title.encode('ascii', 'ignore')
			place = self.dstk.text2places(title)
			if place != []:
				name = pattern.search(title).group()
				lat = place[0]['latitude']
				lon = place[0]['longitude']
				p = Place(image=post.url, name=name, caption=title, latitude=lat, longitude=lon)
				p.save()
				count += 1

		self.stdout.write('Successfully fetched new images')

	def contains(self, image):
		return Place.objects.filter(image=image).count() > 0
