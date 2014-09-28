from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_POST

from models import Place


def index(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
		'countries' : Place.objects.values_list('country', flat=True).distinct(),
	}
	print Place.objects.values_list('country', flat=True).distinct()
	return render(request, 'earthporn/index.html', context)

@require_POST
def country(request):
	print request.POST
	country = request.POST.get('country')
	places = Place.objects.filter(country=country)
	context = {
		'places' : places,
	}
	print country
	print Place.objects.filter(country=country)
	# open carosoul and show images
	return render(request, 'earthporn/country.html', context)
