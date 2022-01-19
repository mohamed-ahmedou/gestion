from multiprocessing import context
from sqlite3 import PARSE_COLNAMES
from django.shortcuts import render
from django.http import HttpResponse

from Bourse.forms import FactureForm

from .models import * 
from .forms import FactureForm
def home(request):
    client = Client.objects.all()
    facture = Facture.objects.all()
    t_facture = facture.count()
    a_facture = facture.filter(type='ACHAT').count()
    v_facture = facture.filter(type='VENDRE').count() 
    context = {'client':client,
               'facture':facture,
               't_facture':t_facture,
               'a_facture':a_facture,
               'v_facture':v_facture}
    
    return render(request ,'Bourse/tabledebord.html',context)
def voitures(request):
    voiture = Voiture.objects.all()
    return render(request, 'Bourse/voiture.html',{'voitures':voiture})

def client(request,pk):
    client = Client.objects.get(id=pk)
    factures = client.facture_set.all()
    nombre_facture = factures.count()
    context = {'client': client,
               'factures': factures,
               'nombre_facture':  nombre_facture }       
    
    return render(request, 'Bourse/Client.html', context)   

def create(request):
   form = FactureForm()
   context = {'form':form}
   return render(request, 'Bourse/mon_form.html',context)