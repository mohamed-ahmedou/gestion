
from webbrowser import Opera
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout

from Bourse.forms import FactureForm

from .models import * 
from .forms import FactureForm
from .filters import FactureFilter
from django.contrib.auth.forms import UserCreationForm
def home(request):
    client = Client.objects.all()
    voiture = Voiture.objects.all()
    facture = Facture.objects.all()
    t_facture = facture.count()
    a_facture = facture.filter(type='ACHAT').count()
    v_facture = facture.filter(type='VENDRE').count() 
    
    N_client = client.count()
    N_voiture = voiture.count()

    
    context = {'client':client,
               'facture':facture,
               't_facture':t_facture,
               'a_facture':a_facture,
               'v_facture':v_facture,
               'N_client':N_client,
               'N_voiture':N_voiture}
    
    return render(request ,'Bourse/tabledebord.html',context)
def voitures(request):
    voiture = Voiture.objects.all()
    return render(request, 'Bourse/voiture.html',{'voiture':voiture})
def image(request):
    image = Image.objects.all()
    return render(request, 'Bourse/voiture.html',{'image':image})
def clientt(request):
    clientt = Client.objects.all()
    return render(request, 'Bourse/Clientt.html',{'clientt':clientt})

def voirevoiture(request):
    voirevoiture = Voiture.objects.all()
    return render(request, 'Bourse/voirevoiture.html',{'voirevoiture':voirevoiture})

def operation(request,v):
    vv =  Voiture.objects.filter(matricule=v)
    # operations = Operation.objects.get(voiture=vv)
    operations = Operation.objects.filter(id=v)
    # operation = Operation.objects.filter()
    
    # voiture = Voiture.objects.get(id=pk)  
    # operations = voiture.operation_set.all()
    # nombre_operation = operations.count()
    # context = {'operation' : operation,
    #            'voiture': voiture,
    #            'operations': operations,
    #            'nombre_operation':  nombre_operation }           
    return render(request, 'Bourse/operation.html', {'operations':operations}) 

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
    voiture = Voiture.objects.all()
    facture = Facture.objects.all()
    t_facture = facture.count()
    a_facture = facture.filter(type='ACHAT').count()
    v_facture = facture.filter(type='VENDRE').count() 
    
    N_client = client.count()
    N_voiture = voiture.count()

    
    context = {'client':client,
               'facture':facture,
               't_facture':t_facture,
               'a_facture':a_facture,
               'v_facture':v_facture,
               'N_client':N_client,
               'N_voiture':N_voiture,}
    
    return render(request, 'Bourse/tabledebord.html', context)

def login(request):

    # if request.user.is_authenticated:
    #   return redirect("/home/")  
    if request.method == "POST":
        user = request.POST['username']
        passs = request.POST['password']
        user = authenticate(username=user, password=passs)
        if user is not None:
            if user.is_superuser:
                # auth_login(request, user)
                return redirect("/home/")
                # return render(request, 'Bourse/tabledebord.html')
        else:   
            msg = "Les données sont  erronés,ressayer"
            return render(request, "Bourse/login.html", {"msg":msg})
    return render(request, "Bourse/login.html")
    

def register(request):  
    context = {}
    return render(request, 'Bourse/register.html',context)
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    # # context = {'form', form}
    # return render(request, 'Bourse/regis.html',context)