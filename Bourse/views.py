from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request ,'Bourse/tabledebord.html')
def voiture(request):
    return render(request, 'Bourse/voiture.html')
# def users(request):
#     return HttpResponse('users page pour Bource)')
def client(request):
    return render (request , 'Bourse/Client.html')   
def elouss6oura(request):
    return HttpResponse("<h1> Elouss6ouraaaaaa (Bource) </h1>")
# Create your views here.
