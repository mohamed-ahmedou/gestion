from django.contrib import admin

from .models import User, facture, voiture, image, operation

class operationaff(admin.ModelAdmin):
    list_display = ('nom','Date')
class factureaff(admin.ModelAdmin):
    list_display = ('id_user','id_voiture','type','Date')
class useraff(admin.ModelAdmin):
    list_display = ('type','nom','prenom','email','tel','id_voiture')
class voitureaff(admin.ModelAdmin):
    list_display = ('id_image','id_operation','matricule','Marque','couleur','prix','modele','numerosachet')
# class imageaff(admin.ModelAdmin):
#     list_display = ('url')

admin.site.register(User,useraff)
admin.site.register(facture,factureaff)
admin.site.register(voiture,voitureaff)
admin.site.register(image)
admin.site.register(operation,operationaff)
# @admin.register(Todo, TodoList)
# class GenricAdmin(admin.ModelAdmin):
#     pass

# Register your models here.
