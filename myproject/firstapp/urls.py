from django.urls import path,include
from .import views



urlpatterns = [

   
    path('',views.index,name='index'),
    path('create-form/',views.create_contact,name='create-contact'),    
   
  

]
