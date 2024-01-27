from django.urls import path
from . import views

urlpatterns = [
    path('demrdv/',views.DemRdvView , name='demrdv'),
    path('pagesucc/',views.successView , name='pagesuc'),
    path('medecin/<int:medecin_id>/', views.medecin_detail, name='medecin_detail'),
    ]
  
