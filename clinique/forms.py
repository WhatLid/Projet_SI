from urllib import request
from django import forms
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  *

class inscriptionForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  


class ConnexionForm(forms.ModelForm):
    class Meta:
        model= Compte
        fields= ['email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'dn', 'specialite', 'departement', 'tel','email']


class rdvForm(forms.ModelForm):
    class Meta:
        model= demRendezVous
        fields= ['date','heure','departement','sujet']



class ConnexionFormmed(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

