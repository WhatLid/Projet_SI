import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_si.settings')
import django
django.setup()

import random
from faker import Faker
from clinique.models import Patient, Departement, Medecin, RendezVous, DossierMedical, ActeMedical, Chirurgie, SalleOperation, Medicament, PrescriptionMedicale, demRendezVous

fake = Faker()

def create_departements():
    departements = ["Cardiologie", "Dermatologie", "Ophtalmologie", "Orthopédie", "Gynécologie"]
    for dep in departements:
        Departement.objects.create(nom=dep)

def create_patients(num_patients):
    for _ in range(num_patients):
        nom = fake.last_name()
        prenom = fake.first_name()
        dn = fake.date_of_birth()
        sexe = random.choice(['F', 'M'])
        adresse = fake.address()
        nss = fake.unique.random_number()
        email = fake.email()
        password = fake.password()

        Patient.objects.create(
            nom=nom, prenom=prenom, dn=dn, sexe=sexe,
            adresse=adresse, nss=nss, email=email, password=password
        )

def create_medecins(num_medecins):
    departements = Departement.objects.all()
    for _ in range(num_medecins):
        nom = fake.last_name()
        prenom = fake.first_name()
        dn = fake.date_of_birth()
        specialite = fake.word()
        tel = fake.phone_number()
        email = fake.email()

        medecin = Medecin.objects.create(
            nom=nom, prenom=prenom, dn=dn, specialite=specialite,
            departement=random.choice(departements), tel=tel, email=email
        )
        medecin.disponibilite = fake.boolean()
        medecin.save()

def create_rendezvous(num_rendezvous):
    patients = Patient.objects.all()
    medecins = Medecin.objects.all()
    departements = Departement.objects.all()

    for _ in range(num_rendezvous):
        patient = random.choice(patients)
        medecin = random.choice(medecins)
        date = fake.date_this_year()
        heure = fake.time()
        departement = random.choice(departements)
        sujet = fake.text()

        RendezVous.objects.create(
            patient=patient, medecin=medecin, date=date,
            heure=heure, departement=departement, sujet=sujet
        )

def create_dossiers_medicaux():
    patients = Patient.objects.all()
    for patient in patients:
        DossierMedical.objects.create(patient=patient, antecedents_medicaux=fake.text(), allergies=fake.text(),
                                       traitements_en_cours=fake.text(), notes_supplementaires=fake.text(),
                                       rhesus_sanguin=random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']))

def create_actes_medicaux(num_actes):
    for _ in range(num_actes):
        nom = fake.word()
        date = fake.date_this_year()
        description = fake.text()

        ActeMedical.objects.create(nom=nom, date=date, description=description)

def create_chirurgies(num_chirurgies):
    for _ in range(num_chirurgies):
        nom = fake.word()
        date = fake.date_this_year()
        description = fake.text()

        Chirurgie.objects.create(nom=nom, date=date, description=description)

def create_salles_operations(num_salles):
    for i in range(1, num_salles + 1):
        nom = f"Salle{i}"
        SalleOperation.objects.create(nom=nom)

def create_medicaments(num_medicaments):
    for _ in range(num_medicaments):
        nom = fake.word()
        posologie = fake.text()

        Medicament.objects.create(nom=nom, posologie=posologie)

def create_prescriptions(num_prescriptions):
    rendezvous = RendezVous.objects.all()
    actes_medicaux = ActeMedical.objects.all()
    chirurgies = Chirurgie.objects.all()
    medicaments = Medicament.objects.all()

    for _ in range(num_prescriptions):
        rendezvous_obj = random.choice(rendezvous)
        actes_medicaux_objs = random.sample(list(actes_medicaux), random.randint(1, 3))
        chirurgies_objs = random.sample(list(chirurgies), random.randint(1, 3))
        medicaments_objs = random.sample(list(medicaments), random.randint(1, 3))

        prescription = PrescriptionMedicale.objects.create(rendezvous=rendezvous_obj)
        prescription.acte_medical.set(actes_medicaux_objs)
        prescription.chirurgie.set(chirurgies_objs)
        prescription.medicaments.set(medicaments_objs)

def create_dem_rendezvous(num_dem_rdv):
    patients = Patient.objects.all()
    departements = Departement.objects.all()

    for _ in range(num_dem_rdv):
        patient = random.choice(patients)
        date = fake.date_this_year()
        heure = fake.time()
        departement = random.choice(departements)
        sujet = fake.text()

        demRendezVous.objects.create(patient=patient, date=date, heure=heure, departement=departement, sujet=sujet)

def main():
    create_departements()
    create_patients(20)
    create_medecins(5)
    create_rendezvous(30)
    create_dossiers_medicaux()
    create_actes_medicaux(10)
    create_chirurgies(10)
    create_salles_operations(5)
    create_medicaments(10)
    create_prescriptions(20)
    create_dem_rendezvous(15)

if __name__ == "__main__":
    main()
