from django.contrib import admin

from .models import Patient, Departement, Medecin, RendezVous, DossierMedical, ActeMedical, Chirurgie, SalleOperation, Medicament, PrescriptionMedicale
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