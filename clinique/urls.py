from django.urls import path

from clinique.admin import AdminMedecin
from . import views

urlpatterns = [
    path('inscription/',views.inscriptionView , name='inscription'),
    path('connexion/',views.connexionView ,name='connexion'),
    path('connexionmed/',views.connexionViewmed,name='connexionmed'),
    path('pagesucc/',views.successView , name='pagesuc'),
    path('profil/', views.profil, name='profil'),
    path('dashboard/' , views.medecin_dashboard_view,name='dashboard'),
    path('home/',views.homeView, name='home'),
    path('connected/',views.connected, name='connected'),
    path('rdv/', views.rdv, name='rdv'),
    path('medecin/<int:medecin_id>/', views.medecin_detail, name='medecin_detail'),
    path('redirect-to-admin-medecin/', views.adminmedecin ,name='adminmedecin'),
    path('afficher_dossier_medical/<str:patient_email>/', views.afficher_dossier_medical, name='afficher_dossier_medical'),
    ]
  
