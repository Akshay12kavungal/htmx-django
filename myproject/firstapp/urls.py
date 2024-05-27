from django.urls import path,include
from .import views
from .views import SchoolListView,SchoolDetailView,SchoolUpdateView,SchoolDeleteView,SchoolCreateView



urlpatterns = [

   
    path('',views.index,name='index'),
    path('create-form/',views.create_contact,name='create-contact'),   
    path('Register/',views.Register,name='Register'),
    path('check_username/', views.check_username, name='check_username'),
    path('login/',views.Login,name='login'),


    #school

    path('school/',SchoolListView.as_view(),name='school_list'),
    path('school/create/', SchoolCreateView.as_view(), name='school_create'),
    path('school/<int:pk>/',SchoolDetailView.as_view(),name='school_detail'),
    path('school/update/<int:pk>/', SchoolUpdateView.as_view(), name='school_update'),
    path('school/delete/<int:pk>/', SchoolDeleteView.as_view(), name='school_delete'),

   
  

]
