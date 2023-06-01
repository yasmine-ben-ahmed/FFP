from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login 
from .models import *

from signup.models import supervisor
from signup.models import client
# from map.models import mPolygons

from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry

def home(request):
    return render(request, 'index.html')







    