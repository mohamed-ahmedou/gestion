from dataclasses import fields
from itertools import product
from pyexpat import model
from unicodedata import name
import django_filters 
from .models import *

class FactureFilter(django_filters.FilterSet):
    class Meta:
        model = Facture
        fields = '__all__'