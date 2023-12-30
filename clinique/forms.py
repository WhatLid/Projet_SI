from django import forms
from .models import DemandeRdv 

class DemRdvForm(forms.ModelForm):
    class Meta:
        model = DemandeRdv
        fields = '__all__'  
