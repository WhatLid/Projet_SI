from django.contrib import admin

from .models import Compte, Patient, Departement, Medecin, RendezVous, DossierMedical, ActeMedical, Chirurgie, SalleOperation, Medicament, PrescriptionMedicale, demRendezVous
# Register your models here.
admin.site.register(Patient)
admin.site.register(Departement)
admin.site.register(Medecin)
admin.site.register(RendezVous)
admin.site.register(DossierMedical)
admin.site.register(ActeMedical)
admin.site.register(Chirurgie)
admin.site.register(SalleOperation)
admin.site.register(Medicament)
admin.site.register(PrescriptionMedicale)
admin.site.register(demRendezVous)
admin.site.register(Compte)