from django import forms
from .models import *

class inscriptionForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  


class ConnexionForm(forms.ModelForm):
    class Meta:
        model= Compte
        fields= '__all__'

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'dn', 'specialite', 'departement', 'tel','email']


class rdvForm(forms.ModelForm):
    class Meta:
        model= demRendezVous
        fields= ['date','heure','departement','sujet']