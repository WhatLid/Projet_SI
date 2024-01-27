from django.shortcuts import render, redirect, get_object_or_404
from .forms import  *

def inscriptionView(request):
    if request.method == 'POST':
        form = inscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagesuc')  
    else:
        form = inscriptionForm()

    #return render(request, 'DemRdv.html', {'form': form}) 
    return render(request, 'inscription.html', {'form': form})


def connexionView(request):
   
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['password']
            
        try:
            patient = Patient.objects.get(email=email, password=password)
        except Patient.DoesNotExist:
            return render(request, 'connexion.html', {'form': form, 'message':'Identifiants incorrects'} )

        return redirect('pagesuc')  
    else:
        form = ConnexionForm()

    #return render(request, 'DemRdv.html', {'form': form}) 
    return render(request, 'connexion.html', {'form': form})  

def successView(request):
    return render(request,'pagesuccess.html')

def medecin_detail(request,medecin_id):
    medecin = get_object_or_404(medecin, pk=medecin_id)
    form = MedecinForm(instance=medecin)

    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            
    return render(request, 'medecin_detail.html', {'medecin': medecin, 'form': form})
