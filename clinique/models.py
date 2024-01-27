from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dn = models.DateField()
    choix_sexe = [('F','Féminin'), ('M', 'Masculin')]
    sexe = models.CharField(max_length=1, choices=choix_sexe, default='F')
    adresse = models.CharField(max_length=100, null=True)
    nss = models.IntegerField(unique=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    password = models.CharField(max_length=128,null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Compte(models.Model):
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=128)

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dn = models.DateField()
    specialite = models.CharField(max_length=100)
    departement=models.ForeignKey(Departement, on_delete=models.CASCADE)
    tel_regex = RegexValidator(
        regex=r'^(05|06|07)[0-9]{8}$',
        message="Le numéro de téléphone doit contenir 10 chiffres commançant par 05 ou 06 ou 07."
    )
    tel = models.CharField(
        validators=[tel_regex],
        max_length=10
    )
    email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message="Veuillez saisir une adresse e-mail valide."
    )
    email = models.EmailField(
        validators=[email_regex]
    )
    disponibilite = models.BooleanField(default=True)
    # prop medecin a ajouter

    def __str__(self):
        return f"{self.nom} {self.prenom}, {self.specialite},{self.departement}"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    sujet = models.TextField(default="")

    def __str__(self):
        return f"{self.patient},{self.date} {self.heure}"

class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Dossier médical de {self.patient.nom} {self.patient.prenom}"

class ActeMedical(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.nom}"

class Chirurgie(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.nom}"
    
class SalleOperation(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Salle {self.nom}"

class Medicament(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    posologie = models.TextField()

    def __str__(self):
        return f"{self.nom}"

class PrescriptionMedicale(models.Model):
    rendezvous = models.OneToOneField(RendezVous, on_delete=models.CASCADE)
    acte_medical = models.ManyToManyField(ActeMedical, blank=True)
    chirurgie = models.ManyToManyField(Chirurgie, blank=True)
    medicaments = models.ManyToManyField(Medicament)



class demRendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    sujet = models.TextField(default="")

    def __str__(self):
        return f"{self.patient},{self.date} {self.heure}"