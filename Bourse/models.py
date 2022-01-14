from typing import List
from django.db import models

from django.db.models.fields.files import ImageField

# Create your models here.
# class Todo(models.Model):
#     title = models.CharField(max_length=255)
#     dve_date = models.DateField()
#     completed = models.BooleanField()
#     favorite = models.BooleanField()
    
#     List = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)
# class TodoList(models.Model):
#     name = models.CharField(max_length=255)

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    tel = models.IntegerField()
    
class voiture(models.Model):
    
    matricule = models.CharField(max_length=50)
    Marque = models.CharField(max_length=40)
    couleur = models.CharField(max_length=60)
    prix = models.FloatField(max_length=40)
    modele = models.CharField(max_length=40)
    numerosachet = models.CharField(max_length=40)
    id_client = models.ForeignKey(Client ,on_delete = models.CASCADE)
    
class image(models.Model):
    url = models.ImageField(upload_to='Bourse/static/image', null=True)
    id_voiture = models.ForeignKey(voiture ,on_delete = models.CASCADE)
    
class operation(models.Model):
    nom = models.CharField(max_length=30)
    Date = models.DateField(max_length=40)
    id_voiture = models.ForeignKey(voiture ,on_delete = models.CASCADE)

    
class facture(models.Model):
    id_client = models.ForeignKey(Client,on_delete = models.CASCADE)
    id_voiture = models.ForeignKey(voiture,on_delete = models.CASCADE)
    type = models.CharField(max_length=50)
    Date = models.DateField(max_length=50)
