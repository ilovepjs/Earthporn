import json

from django.core import serializers
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.views.decorators.http import require_POST

from countries import countries
from porn.models import Place

def index(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
		'countries' : Place.objects.values_list('country', flat=True).distinct(),
	}
	print Place.objects.values_list('country', flat=True).distinct()
	return render(request, 'porn/index.html', context)

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
	return render(request, 'porn/country.html', context)
