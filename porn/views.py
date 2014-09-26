from django.core import serializers
from django.shortcuts import render
from porn.models import Place
from forms import CountryForm
from countries import countries
import json

def index(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
		'countries' : countries.values(),
        'form': CountryForm(),
	}
	return render(request, 'porn/index.html', context)

def country(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
	}
	return render(request, 'porn/index.html', context)