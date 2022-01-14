from django.contrib import admin

from .models import Client, facture, voiture, image, operation

class operationaff(admin.ModelAdmin):
    list_display = ('nom','Date','id_voiture')
class factureaff(admin.ModelAdmin):
    list_display = ('id_client','id_voiture','type','Date')
class clientaff(admin.ModelAdmin):
    list_display = ('nom','prenom','email','tel')
class voitureaff(admin.ModelAdmin):
    list_display = ('matricule','Marque','couleur','prix','modele','numerosachet','id_client')
class imageaff(admin.ModelAdmin):
    list_dsiplay = ('url')
# class imageaff(admin.ModelAdmin):
#     list_display = ('nom')

admin.site.register(Client,clientaff)
admin.site.register(facture,factureaff)
admin.site.register(voiture,voitureaff)
admin.site.register(operation,operationaff)
admin.site.register(image,imageaff)
# @admin.register(Todo, TodoList)
# class GenricAdmin(admin.ModelAdmin):
#     pass

# Register your models here.
