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


class AdminMedecin(admin.AdminSite):
    site_header = 'Admin Medecin'
    site_title = 'Admin Medecin'

adminmedecin = AdminMedecin(name='adminmedecin')


from .models import Patient, Departement, Medecin, RendezVous, DossierMedical, ActeMedical, Chirurgie, SalleOperation, Medicament, PrescriptionMedicale, demRendezVous, Compte
from .admin import admin

adminmedecin.register(Patient)
adminmedecin.register(RendezVous)
adminmedecin.register(DossierMedical)
adminmedecin.register(PrescriptionMedicale)

