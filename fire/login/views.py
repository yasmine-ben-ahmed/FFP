from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from map.models import myProject
from signup.models import client
from django.contrib.auth.forms import PasswordResetForm



def connectas(request):
    return render(request, 'connectas.html', {})

def connectasclient(request):
    
    
    if request.method == 'POST':

        if 'reset_password' in request.POST:
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                form.save(
                    request=request,
                    # email_template_name='password_reset_email.html'
                )
                return render(request, 'password_reset_done.html')
        else:
            formulaire = LoginForm(request.POST)
            if formulaire.is_valid(request):
                pseudo = formulaire.cleaned_data['pseudo']
                mot_de_passe = formulaire.cleaned_data['mot_de_passe']
                data = authenticate(request, username=pseudo,
                                    password=mot_de_passe)
                if data is not None:
                    login(request, data)

                    clientp = client.objects.get(pseudo=pseudo)
                    # project = myProject.objects.get(clientp=clientp)
                    
                return redirect('client_project',pseudo)
            # We pass the form to the template even if it is not valid
            return render(request, 'login_client.html', {'form': formulaire})

    else:
        form = PasswordResetForm()
    # We pass the form to the template for GET requests
    return render(request, 'login_client.html', {'form': LoginForm()})


def connectassupervisor(request):
    if request.method == 'POST':

        if 'reset_password' in request.POST:
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                form.save(
                    request=request,
                    email_template_name='password_reset_email.html'
                )
                return render(request, 'password_reset_done.html')
        else:
            formulaire = LoginFormSup(request.POST)
            if formulaire.is_valid(request):
                pseudo = formulaire.cleaned_data['pseudo']
                mot_de_passe = formulaire.cleaned_data['mot_de_passe']
                data = authenticate(request, username=pseudo,
                                    password=mot_de_passe)
                if data is not None:
                    login(request, data)
                return redirect('display',pseudo)
            # We pass the form to the template even if it is not valid
            return render(request, 'login_superviseur.html', {'form': formulaire})
    else:
        form = PasswordResetForm()
    # We pass the form to the template for GET requests
    return render(request, 'login_superviseur.html', {'form': LoginFormSup()})





