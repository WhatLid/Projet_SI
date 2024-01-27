from django.urls import path
from . import views

urlpatterns = [
    path('inscription/',views.inscriptionView , name='inscription'),
    path('connexion/',views.connexionView ,name='connexion'),
    path('pagesucc/',views.successView , name='pagesuc'),
    path('profil/', views.profil, name='profil'),
    path('medecin/<int:medecin_id>/', views.medecin_detail, name='medecin_detail'),
    ]
  
