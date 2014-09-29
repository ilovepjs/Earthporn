from django.core import serializers
from django.shortcuts import render
from django.views.decorators.http import require_POST

from models import Place


def index(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
		'countries' : Place.objects.values_list('country', flat=True).distinct(),
	}
	return render(request, 'earthporn/index.html', context)

def country(request, country_name):
	places = Place.objects.filter(country=country_name)
	context = {
		'places' : places,
	}
	return render(request, 'earthporn/country.html', context)
