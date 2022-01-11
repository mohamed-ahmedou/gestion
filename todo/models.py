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

class image(models.Model):
    url = models.ImageField(upload_to='todo/static/image', null=True)
class operation(models.Model):
    nom = models.CharField(max_length=30)
    Date = models.DateField(max_length=40)
    
class voiture(models.Model):
    id_image = models.ForeignKey(image ,on_delete = models.CASCADE)
    id_operation = models.ForeignKey(operation ,on_delete = models.CASCADE)
    matricule = models.CharField(max_length=50)
    Marque = models.CharField(max_length=40)
    couleur = models.CharField(max_length=60)
    prix = models.FloatField(max_length=40)
    modele = models.CharField(max_length=40)
    numerosachet = models.CharField(max_length=40)
    
class User(models.Model):
    type = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    tel = models.IntegerField()
    id_voiture = models.ForeignKey(voiture ,on_delete = models.CASCADE)

    
class facture(models.Model):
    id_user = models.ForeignKey(User,on_delete = models.CASCADE)
    id_voiture = models.ForeignKey(voiture,on_delete = models.CASCADE)
    type = models.CharField(max_length=50)
    Date = models.DateField(max_length=50)
    