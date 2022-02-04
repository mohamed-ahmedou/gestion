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
    
    def __str__(self):
        return self.nom
        
    
class Voiture(models.Model):
    matricule = models.CharField(max_length=50)
    marque = models.CharField(max_length=50)
    couleur = models.CharField(max_length=60)
    prix = models.FloatField(max_length=40)
    modele = models.CharField(max_length=40)
    numerosachet = models.CharField(max_length=40)
    image = models.ImageField(upload_to='static/image', null=True)
    # client = models.ForeignKey(Client ,related_name='voitures', on_delete=models.CASCADE)
    def __str__(self):
      return self.modele
    
class Image(models.Model):
    url = models.ImageField(upload_to='static/image', null=True)
    voiture = models.ForeignKey(Voiture ,related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
          return self.voiture

		
class Operation(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    voiture = models.ForeignKey(Voiture, null=True, on_delete=models.SET_NULL)
	
    def __str__(self):
        return self.nom

    
    
class Facture(models.Model):
	
	# ACHAT = 'achat'
	# VENDRE = 'vendre'
	
    FACTURE_TYPE = (
        ('ACHAT', 'Achat'),
        ('VENDRE', 'Vendre')
    )
	
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    voiture = models.ForeignKey(Voiture ,related_name='factures', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=FACTURE_TYPE)
    date = models.DateTimeField(auto_now_add=True)

	
    def __str__(self):
        return self.type

#  client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
#  client = models.ForeignKey(Client ,related_name='factures', on_delete=models.CASCADE)