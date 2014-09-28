from django.db import models

class Place(models.Model):
	image = models.CharField(max_length=400, primary_key=True)
	name = models.CharField(max_length=200)
	caption = models.CharField(max_length=1200)
	latitude = models.FloatField()
	longitude = models.FloatField()
	country = models.ForeignKey('Country')

	def __unicode__(self):
		return '{} ({}, {}): {}'.format(
			self.caption, self.latitude, self.longitude, self.image)

class Country(models.Model):
	id = models.CharField(max_length=400, primary_key=True)

	def __unicode__(self):
		return self.id