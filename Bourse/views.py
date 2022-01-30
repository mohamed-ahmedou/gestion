
from contextlib import redirect_stderr
import email
from webbrowser import Opera
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout

from Bourse.forms import FactureForm

from .models import * 
from .forms import FactureForm
from .forms import *
from .filters import FactureFilter
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import VoitureForm
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

def gerervoitures(request):
    voituree = Voiture.objects.all()
    return render(request, 'Bourse/gerervoitures.html',{'voituree':voituree})

# def image(request):
#     image = Image.objects.all()
#     return render(request, 'Bourse/voiture.html',{'image':image})
def clientt(request):
    clientt = Client.objects.all()
    return render(request, 'Bourse/Clientt.html',{'clientt':clientt})

def voirevoiture(request,myid):
    vv = Voiture.objects.get(id=myid)
    return render(request, 'Bourse/voirevoiture.html',{'vv':vv})

def operation(request,v):
    vv =  Voiture.objects.filter(matricule=v)
    operations = Operation.objects.filter(id=v)     
    return render(request, 'Bourse/operation.html', {'operations':operations}) 

def client(request,pk):
    client = Client.objects.get(id=pk)
    factures = client.facture_set.all()
    nombre_facture = factures.count()
    context = {'client': client,
               'factures': factures,
               'nombre_facture':  nombre_facture }           
    return render(request, 'Bourse/Client.html', context)   


def Ajoutvoiture(request):
    if request.method=="POST":   
        matricule = request.POST['matricule']
        marque = request.POST['marque']
        couleur=request.POST['couleur']
        prix=request.POST['prix']
        modele=request.POST['modele']
        numerosachet = request.POST['numerosachet']
        image = request.POST['image']
        c = Voiture.objects.create(matricule=matricule,  marque= marque, couleur = couleur,prix=prix ,modele = modele ,numerosachet = numerosachet, image = image )
        c.save()
        return redirect("/gerervoitures")  
    return render(request, 'Bourse/Ajoutvoiture.html')

def Modifiervoiture(request, myid):
    v = Voiture.objects.get(id=myid)
    if request.method=="POST":   
        v.matricule = request.POST['matricule']
        v.marque = request.POST['marque']
        v.couleur=request.POST['couleur']
        v.prix=request.POST['prix']
        v.modele=request.POST['modele']
        v.numerosachet = request.POST['numerosachet']
        v.image = request.POST['image']
        v.save()
        return redirect("/gerervoitures")  
    return render(request, 'Bourse/modifiervoitures.html', {'v': v})

def supprimervoiture(request, myid):
    voiture = Voiture.objects.filter(id=myid)
    voiture.delete()
    return redirect("/gerervoitures")  

def Ajoutclient(request):
    if request.method=="POST":   
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email=request.POST['email']
        tel = request.POST['tel']
        c = Client.objects.create(nom=nom,  prenom = prenom, email = email, tel = tel)
        c.save()
        return redirect("/clientt")  
    return render(request, 'Bourse/Ajoutclient.html')

def modifierclient(request, myid):
    v = Client.objects.get(id=myid)
    if request.method=="POST":   
        v.nom = request.POST['nom']
        v.prenom = request.POST['prenom']
        v.email=request.POST['email']
        v.tel=request.POST['tel']
        v.save()
        return redirect("/clientt")  
    return render(request, 'Bourse/modifierclient.html', {'v': v})

def supprimerclient(request, myid):
    client = Client.objects.filter(id=myid)
    client.delete()
    return redirect("/clientt")  

def ajouter(request):
   form = FactureForm()
   if request.method == 'POST':
       form = FactureForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("/home")
   conntext = {'form':form}
   return render(request, 'Bourse/mon_form.html',conntext)

def modifier(request,pk):
    facture = Facture.objects.get(id=pk)
    form = FactureForm(instance=facture) 
    if request.method == 'POST':
           form = FactureForm(request.POST, instance=facture)
           if form.is_valid():
              form.save()
                  
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
    conttext = {'form':form}
    return render(request, 'Bourse/mon_form.html',conttext)

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
                return redirect("/home")
                # return render(request, 'Bourse/tabledebord.html')
        else:   
            msg = "Les données sont  erronés,ressayer"
            return render(request, "Bourse/login.html", {"msg":msg})
    return render(request, "Bourse/login.html")
    

def register(request):  
    context = {}
    return render(request, 'Bourse/register.html',context)
   