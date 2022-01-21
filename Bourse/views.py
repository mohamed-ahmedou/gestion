
from django.shortcuts import render, redirect
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

def ajouter(request):
   form = FactureForm()
   if request.method == 'POST':
       form = FactureForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')
   context = {'form':form}
   return render(request, 'Bourse/mon_form.html',context)

def modifier(request,pk):
    facture = Facture.objects.get(id=pk)
    form = FactureForm(instance=facture) 
    if request.method == 'POST':
           form = FactureForm(request.POST, instance=facture)
           if form.is_valid():
              form.save()
              return redirect('/')
    context = {'form':form}
    return render(request, 'Bourse/mon_form.html',context)

def confirmersupression(request,pk):
    pk = pk 
    return render(request, 'Bourse/supprimer_form.html',{'pk': pk})

def supprimer(request,pk):
    
    facture = Facture.objects.filter(id=pk)
    facture.delete()
    
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
    
    return render(request, 'Bourse/tabledebord.html', context)