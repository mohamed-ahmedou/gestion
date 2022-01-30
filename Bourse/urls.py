from unicodedata import name
from django.urls import path
from .views import *



 
from . import views

urlpatterns = [ 
    path('home/', views.home, name="home"),
    path('', views.voitures, name="voiture"),  
    path('client/<str:pk>',views.client, name="client"), 
    path('gerervoitures/', views.gerervoitures, name="voiture"),
    path('ajouter',views.ajouter, name="ajouter"),
    path('modifier/<str:pk>',views.modifier, name="modifier"),
    path('confirmersupression/<int:pk>/',views.confirmersupression, name="confirmersupression"),
    path('supprimer/<int:pk>/',views.supprimer, name="supprimer"),
    path('login/',views.login , name="login"),
    path('register/',views.register, name="register"),
    path('clientt/',views.clientt, name="clientt"),
    path('operation/',views.operation, name="operation"),
    path('operation/<str:v>/',views.operation, name="operation"),
    path('voirevoiture/<str:myid>',views.voirevoiture, name="voirevoiture"),
    path('Ajoutvoiture/',views.Ajoutvoiture, name="Ajoutvoiture"),
    path('Modifiervoiture/<int:myid>/',views.Modifiervoiture, name="Modifiervoiture"),
    path('supprimervoiture/<int:myid>/',views.supprimervoiture, name="supprimervoiture"),
    path('Ajoutclient/',views.Ajoutclient, name="Ajoutclient"),
    path('modifierclient/<int:myid>/',views.modifierclient, name="modifierclient"),
    path('supprimerclient/<int:myid>/',views.supprimerclient, name="supprimerclient"),
    # path('Elouss6oura',views.elouss6oura),
]