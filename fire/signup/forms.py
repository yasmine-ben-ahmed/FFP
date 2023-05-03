from django import forms
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import *

class Form_supervisor(forms.Form):
    nom = forms.CharField(required=True, max_length=supervisor._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;", 'placeholder': 'Last Name'}))
    
    prenom = forms.CharField(required=True, max_length=supervisor._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'First Name', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    telephone = forms.CharField(required=True, max_length=supervisor._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Phone', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    pseudo = forms.CharField(required=True, max_length=supervisor._meta.get_field(
        'pseudo').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    email = forms.EmailField(max_length=supervisor._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'Mail', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Password', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-enter password', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))


    def is_valid(self):
            nom = self.data['nom']
            if any(char.isdigit() for char in nom):
                self.add_error("nom", "Nom est incorrect!")
            prenom = self.data['prenom']
            if any(char.isdigit() for char in prenom):
                self.add_error("prenom", "Prenom est incorrect!")
            pseudo = self.data['pseudo']
            if supervisor.objects.filter(pseudo=pseudo).exists():
                self.add_error("pseudo", "pseudo déja existant!")
            email = self.data['email']
            if supervisor.objects.filter(e_mail=email).exists():
                self.add_error("email", "email déja existant!")
            telephone = self.data['telephone']
            if not telephone.isdigit():
                self.add_error("telephone", "Téléphone est incorrect!")
            mot_de_passe = self.data['mot_de_passe']
            if len(mot_de_passe) < 8:
                self.add_error(
                    "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
            confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
            if confirmation_mot_de_passe != mot_de_passe:
                self.add_error("confirmation_mot_de_passe",
                            "Les mots de passe ne correspondent pas.")
            value = super(Form_supervisor, self).is_valid()
            return value


    def enregistrer(self):
            nom = self.cleaned_data['nom']
            prenom = self.cleaned_data['prenom']
            email = self.cleaned_data['email']
            pseudo = self.cleaned_data['pseudo']
            telephone = self.cleaned_data['telephone']
            confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
            data = supervisor(nom=nom, prenom=prenom, pseudo=pseudo,
                            NB_GSM=telephone, e_mail=email)
            data.save()
            data = User.objects.create_user(
                pseudo, email, confirmation_mot_de_passe)
            data.save()



class Form_client(forms.Form):
    nom = forms.CharField(required=True, max_length=client._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;", 'placeholder': 'Last Name'}))
    
    prenom = forms.CharField(required=True, max_length=client._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'First Name', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    telephone = forms.CharField(required=True, max_length=client._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Phone', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    pseudo = forms.CharField(required=True, max_length=client._meta.get_field(
        'pseudo').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    email = forms.EmailField(max_length=client._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'Mail', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Password', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))
    
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-enter password', 'class': "form-control shadow-lg p-6 mb-4 rounded", 'style': "font-size: 20px; background-color: #DFD9DB;"}))

    def is_valid(self):
            nom = self.data['nom']
            if any(char.isdigit() for char in nom):
                self.add_error("nom", "Nom est incorrect!")
            prenom = self.data['prenom']
            if any(char.isdigit() for char in prenom):
                self.add_error("prenom", "Prenom est incorrect!")
            pseudo = self.data['pseudo']
            if client.objects.filter(pseudo=pseudo).exists():
                self.add_error("pseudo", "pseudo déja existant!")
            email = self.data['email']
            if client.objects.filter(e_mail=email).exists():
                self.add_error("email", "email déja existant!")
            telephone = self.data['telephone']
            if not telephone.isdigit():
                self.add_error("telephone", "Téléphone est incorrect!")
            mot_de_passe = self.data['mot_de_passe']
            if len(mot_de_passe) < 8:
                self.add_error(
                    "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
            confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
            if confirmation_mot_de_passe != mot_de_passe:
                self.add_error("confirmation_mot_de_passe",
                            "Les mots de passe ne correspondent pas.")
            value = super(Form_client, self).is_valid()
            return value


    def enregistrer(self):
            nom = self.cleaned_data['nom']
            prenom = self.cleaned_data['prenom']
            email = self.cleaned_data['email']
            pseudo = self.cleaned_data['pseudo']
            telephone = self.cleaned_data['telephone']
            confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
            data = client(nom=nom, prenom=prenom, pseudo=pseudo,
                            NB_GSM=telephone, e_mail=email)
            data.save()
            data = User.objects.create_user(
                pseudo, email, confirmation_mot_de_passe)
            data.save()
