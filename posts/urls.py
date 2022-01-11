from django.urls import path
# from .views import about, home, users, about
from . import views
urlpatterns = [ 
    path('home/', views.home),
    path('users/', views.users), 
    path('about/',views.about),
    path('',views.elouss6oura)
    
        # path('',home, name='home')

]
#   path('home/',home),
#     path('users/',users),
#     path('about/',about),
#     path('',elouss6oura),