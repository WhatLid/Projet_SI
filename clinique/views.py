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

            request.session['patient_email'] = email
            return redirect('profil')
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


def profil(request):
    # Récupérer le patient avec l'email donné
    patient_email = request.session.get('patient_email', None)
    patient = get_object_or_404(Patient, email=patient_email)

    # Passer le patient à la template
    return render(request, 'profil.html', {'patient': patient})


def rdv(request):
    if request.method == 'POST':
        form = rdvForm(request.POST)
        if form.is_valid():
            patient_email = request.session.get('patient_email', None)

            patient = Patient.objects.get(email=patient_email)
            rdv = form.save(commit=False)
            rdv.patient = patient
            rdv.save()
            
            return redirect('pagesuc')  
    else:
        form = rdvForm()

    #return render(request, 'DemRdv.html', {'form': form}) 
    return render(request, 'rdv.html', {'form': form})




def connexionViewmed(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            # Le formulaire a passé la validation, le compte est un compte de médecin
            # Vous pouvez ajouter d'autres actions ici, par exemple, définir une session, etc.
            return redirect('pagesuc')
    else:
        form = ConnexionForm()

    return render(request, 'connexionmed.html', {'form': form})
