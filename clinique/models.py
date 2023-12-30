from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dn = models.DateField()
    nss = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dn = models.DateField()
    specialite = models.CharField(max_length=100)
    departement=models.CharField(max_length=50, default='Département Temporaire')
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
    departement=models.CharField(max_length=50, default='Département Temporaire')


    def __str__(self):
        return f"{self.patient},{self.date} {self.heure}"

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Dossier médical de {self.patient.nom} {self.patient.prenom}"


class DemandeRdv(models.Model):
    nom= models.CharField(max_length=10)
    prenom= models.CharField(max_length=10)
    tel_regex = RegexValidator(
        regex=r'^(05|06|07)[0-9]{8}$',
        message="Le numéro de téléphone doit contenir 10 chiffres commançant par 05 ou 06 ou 07."
    )
    tel = models.CharField(
        validators=[tel_regex],
        max_length=10
    )
    date= models.DateField()
    heure=models.TimeField()
    Departement=models.CharField(max_length=10)
    sujet=models.CharField(max_length=250)
    