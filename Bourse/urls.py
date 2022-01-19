from unicodedata import name
from django.urls import path
from .views import *

# urlpatterns = [
#     path('',home, name='home')
# ]

from . import views
urlpatterns = [ 
    path('', views.home, name="home"),
    path('voiture/', views.voitures, name="voiture"), 
    path('client/<str:pk>',views.client, name="client"), 
     path('create',views.create, name="create"), 
    # path('Elouss6oura',views.elouss6oura),
]