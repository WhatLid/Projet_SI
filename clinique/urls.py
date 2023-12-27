from django.urls import path
from . import views

urlpatterns = [
    path('liste_medecins/',views.liste_medecins),
    path('liste_patients/',views.liste_patients),
    
]
