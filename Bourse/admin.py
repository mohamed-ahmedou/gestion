from django.contrib import admin

from .models import *

class operationaff(admin.ModelAdmin):
    list_display = ('nom','date','voiture')
class factureaff(admin.ModelAdmin):
    list_display = ('client','voiture','type','date')
class clientaff(admin.ModelAdmin):
    list_display = ('nom','prenom')
class voitureaff(admin.ModelAdmin):
    list_display = ('matricule','marque','couleur','prix','modele','numerosachet','client')
class imageaff(admin.ModelAdmin):
    list_display = ('url','voiture')

admin.site.register(Client)
admin.site.register(Facture)
admin.site.register(Voiture)
admin.site.register(Operation)
admin.site.register(Image)
# @admin.register(Todo, TodoList)
# class GenricAdmin(admin.ModelAdmin):
#     pass

# Register your models here.

