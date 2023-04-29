from django.shortcuts import render, redirect
from .forms import *
#from .models import myPolygon
#from django.contrib.gis.geos import GEOSGeometry

# Create your views here.
def compte(request, pk):
    if pk == 'supervisor':
        if request.method == 'POST':
            formulaire = Form_supervisor(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'supervisor'
                #######PB here
                return redirect('add_client',pseudo)
                # return redirect('map', variable, pseudo)
            return render(request, 'signup.html', {'form': formulaire})
        return render(request, 'signup.html', {'form': Form_supervisor()})
    else:
        if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'client'
                ####### redirect dashboard normally
                #return redirect('map/',variable, pseudo)
                return redirect('interface_c')
            return render(request, 'signup.html', {'form': formulaire})
        return render(request, 'signup.html', {'form': Form_client()})
    

