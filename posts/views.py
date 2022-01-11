from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
def home(request):
    return HttpResponse("ALLAH")
def home(request):
    return HttpResponse('home page')
def users(request):
    return HttpResponse('users page ')
def about(request):
    return HttpResponse("about page")    
def elouss6oura(request):
    return HttpResponse("<h1> Elouss6ouraa </h1>")
# Create your views here.
