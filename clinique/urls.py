from django.urls import path
from . import views

urlpatterns = [
    path('demrdv/',views.DemRdvView , name='demrdv'),
    path('pagesucc/',views.successView , name='pagesuc'),  
    ]
  
