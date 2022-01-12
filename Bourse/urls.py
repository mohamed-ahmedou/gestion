from django.urls import path
from .views import home

# urlpatterns = [
#     path('',home, name='home')
# ]
from . import views
urlpatterns = [ 
    path('', views.home),
    path('voiture/', views.voiture), 
    path('client/',views.client),
    # path('Elouss6oura',views.elouss6oura),
]