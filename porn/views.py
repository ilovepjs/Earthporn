from django.core import serializers
from django.shortcuts import render
from porn.models import Place
import json

def index(request):
	context = {
        'places': serializers.serialize('json', Place.objects.all()),
    }
  	return render(request, 'porn/index.html', context)
