from dataclasses import fields
from multiprocessing.connection import Client
from django.forms import ModelForm, forms
from .models import Facture, Client, Voiture
from django import forms  
from.models import Voiture
class FactureForm(ModelForm):
    class Meta:
        model = Facture
        fields = "__all__"
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        
class VoitureForm(ModelForm):
    class Meta:
        model = Voiture
        fields = ('matricule','marque','couleur','prix','modele','numerosachet','image')
        