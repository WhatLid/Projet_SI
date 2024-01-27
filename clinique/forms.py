from django import forms
from .models import RendezVous, Medecin

class DemRdvForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = '__all__'  

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'dn', 'specialite', 'departement', 'tel','email']