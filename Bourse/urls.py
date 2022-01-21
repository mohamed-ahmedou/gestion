from unicodedata import name
from django.urls import path
from .views import *


# urlpatterns = [
#     path('',home, name='home')
# ]
 
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('voiture/', views.voitures, name="voiture"), 
    path('client/<str:pk>',views.client, name="client"), 
    path('ajouter',views.ajouter, name="ajouter"),
    path('modifier/<str:pk>',views.modifier, name="modifier"),
    path('confirmersupression/<int:pk>/',views.confirmersupression, name="confirmersupression"),
    path('supprimer/<int:pk>/',views.supprimer, name="supprimer"),
    # path('Elouss6oura',views.elouss6oura),
]