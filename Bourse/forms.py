from dataclasses import fields
from multiprocessing.connection import Client
from django.forms import ModelForm
from .models import Facture, Client
    
class FactureForm(ModelForm):
    class Meta:
        model = Facture
        fields = "__all__"
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"