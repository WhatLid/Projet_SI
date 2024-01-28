from django.urls import path
from . import views

urlpatterns = [
    path('inscription/',views.inscriptionView , name='inscription'),
    path('connexion/',views.connexionView ,name='connexion'),
    path('connexionmed/',views.connexionViewmed,name='connexionmed'),
    path('pagesucc/',views.successView , name='pagesuc'),
    path('profil/', views.profil, name='profil'),
    path('dashboard/' , views.medecin_dashboard_view,name='dashboard'),
    path('home/',views.homeView, name='home'),
    path('rdv/', views.rdv, name='rdv'),
    path('medecin/<int:medecin_id>/', views.medecin_detail, name='medecin_detail'),
    ]
  
