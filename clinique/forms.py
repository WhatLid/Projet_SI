from django import forms
from .models import *

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



class ConnexionForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Vérifier si le compte est un compte de médecin
        try:
            compte = Compte.objects.get(email=email, password=password, est_medecin=True)
            medecin = Medecin.objects.get(email=email)
        except Compte.DoesNotExist:
            raise forms.ValidationError("Identifiants incorrects pour un médecin")

        return cleaned_data