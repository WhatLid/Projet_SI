from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import DossierMedical
from .forms import  *

def inscriptionView(request):
    if request.method == 'POST':
        form = inscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['patient_email'] = email
            form.save()

            return redirect('profil')  
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
    rendezvous = RendezVous.objects.filter(patient=patient)

    # Passer le patient à la template
    return render(request, 'profil.html', {'patient': patient, 'rendezvous': rendezvous})


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




""" def connexionViewmed(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            

            return redirect('dashboard')
    else:
        form = ConnexionForm()

    return render(request, 'connexionmed.html', {'form': form}) """


def connexionViewmed(request):
    if request.method == 'POST':
        form = ConnexionFormmed(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                """ compte = Compte.objects.get(email=email, password=password, est_medecin=True) """
                medecin = Medecin.objects.get(email=email , password=password)

                # Sauvegarder l'email dans la session
                request.session['medecin_email'] = email

                return redirect('dashboard')
            except Medecin.DoesNotExist:
                form.add_error(None, "Identifiants incorrects pour un médecin")

    else:
        form = ConnexionForm()

    return render(request, 'connexionmed.html', {'form': form})



""" def medecin_dashboard_view(request):
    # Récupérer le médecin connecté (vous pouvez utiliser le système d'authentification de Django)

    medecin_email = request.session.get('medecin_email', None)

    medecin = Medecin.objects.get(email=medecin_email)
    # Récupérer les rendez-vous et les patients associés au médecin
    rendezvous = medecin.rendezvous_set.all()

    
    patients = medecin.patient_set.all()

    context = {
        'medecin': medecin,
        'rendezvous': rendezvous,
        'patients': patients,
    }

    return render(request, 'dashboard.html', context) """


def medecin_dashboard_view(request):
    # Récupérer le médecin connecté (tu peux utiliser le système d'authentification de Django)
    medecin_email = request.session.get('medecin_email', None)
    medecin = Medecin.objects.get(email=medecin_email)

    # Récupérer les rendez-vous associés au médecin
    rendezvous = RendezVous.objects.filter(medecin=medecin)

    # Récupérer les patients associés aux rendez-vous
    patients = [rdv.patient for rdv in rendezvous]

    context = {
        'medecin': medecin,
        'rendezvous': rendezvous,
        'patients': patients,
        
    }

    return render(request, 'dashboard.html', context)



def homeView(request):
    return render(request,'home.html')

def connected(request):
    return render(request,'connected.html')


def adminmedecin(request):
    return redirect('/adminmedecin/')




""" def afficher_dossier_medical(request, patient_email):
    patient = get_object_or_404(User, email=patient_email)
    dossier_medical = get_object_or_404(DossierMedical, patient=patient)
    return render(request, 'dossiermedical.html', {'patient': patient, 'dossier_medical': dossier_medical}) """

def afficher_dossier_medical(request, patient_email):
    # Récupérer le patient avec l'email donné
    patient = get_object_or_404(Patient, email=patient_email)

    # Récupérer le dossier médical du patient
    dossier = get_object_or_404(DossierMedical, patient=patient)

    return render(request, 'dossiermedical.html', {'patient': patient, 'dossier': dossier})

