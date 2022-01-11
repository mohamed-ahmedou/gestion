from django.urls import path
from .views import home

# urlpatterns = [
#     path('',home, name='home')
# ]
from . import views
urlpatterns = [ 
    path('home/', views.home),
    path('users/', views.users), 
    path('about/',views.about),
    path('Elouss6oura',views.elouss6oura)
    
]