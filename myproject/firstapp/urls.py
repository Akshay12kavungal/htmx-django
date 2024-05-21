from django.urls import path,include
from .import views



urlpatterns = [

   
    path('',views.index,name='index'),
    path('create-form/',views.create_contact,name='create-contact'),   
    path('Register/',views.Register,name='Register'),

    path('check_username/', views.check_username, name='check_username'),
    path('login/',views.Login,name='login'),


 
   
  

]
