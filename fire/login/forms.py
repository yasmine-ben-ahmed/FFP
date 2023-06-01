from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from signup.models import *


class LoginForm(forms.Form):
    pseudo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'pseudo',
                'name': 'pseudo',
                'placeholder': 'Pseudo',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px; background-color: white;"
            }
        )
    )
    mot_de_passe = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Mot de passe',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px; background-color: white;"
            }
        )
    )

    reset_password = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(),
        initial=False,
        label='Forgot Password ?'
    )




    def is_valid(self, request):
        pseudo = self.data['pseudo']
        mot_de_passe = self.data['mot_de_passe']

        if User.objects.filter(username=pseudo).exists() and client.objects.filter(pseudo=pseudo).exists():
            # Here, we assign the result of authenticate() to a variable
            user = authenticate(request, username=pseudo,
                                password=mot_de_passe)
            if user is None:
                self.add_error(
                    "mot_de_passe", "The passwords do not match.")
        else:
            self.add_error("pseudo", "This account does not exist.")
        return super(LoginForm, self).is_valid()




        #----------------------------------------------------------------------------------


class LoginFormSup(forms.Form):
    pseudo = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'pseudo',
                'name': 'pseudo',
                'placeholder': 'Pseudo',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px; background-color: white;"
            }
        )
    )
    mot_de_passe = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'name': 'password',
                'placeholder': 'Mot de passe',
                'class': "form-control shadow-lg p-6 mb-6 rounded",
                'style': "font-size: 20px; background-color: white;"
            }
        )
    )

    reset_password = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(),
        initial=False,
        label='Forgot Password ?'
    )




    def is_valid(self, request):
        pseudo = self.data['pseudo']
        mot_de_passe = self.data['mot_de_passe']

        if User.objects.filter(username=pseudo).exists() and supervisor.objects.filter(pseudo=pseudo).exists():
            # Here, we assign the result of authenticate() to a variable
            user = authenticate(request, username=pseudo,
                                password=mot_de_passe)
            if user is None:
                self.add_error(
                    "mot_de_passe", "The passwords do not match.")
        else:
            self.add_error("pseudo", "This account does not exist.")
        return super(LoginFormSup, self).is_valid()

