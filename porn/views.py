import json

from django.core import serializers
from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.views.decorators.http import require_POST

from countries import countries
from porn.models import Place

def index(request):
	context = {
		'places': serializers.serialize('json', Place.objects.all()),
		'countries' : countries.values(),
	}
	return render(request, 'porn/index.html', context)

@require_POST
def country(request):
	country = request.POST.get('country')
	# open carosoul and show images
	return redirect('/')