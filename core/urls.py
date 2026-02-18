from django.urls import path
from . import views

urlpatterns = [

     path('', views.landing, name='landing'),



    path('donors/', views.donor_list, name='donor_list'),
    path('create/', views.donor_create, name='donor_create'),
    path('update/<int:pk>/', views.donor_update, name='donor_update'),
    path('delete/<int:pk>/', views.donor_delete, name='donor_delete'),
    
    # Recipient URLs
    path('recipients/', views.recipient_list, name='recipient_list'),
    path('recipients/create/', views.recipient_create, name='recipient_create'),
    path('recipients/update/<int:pk>/', views.recipient_update, name='recipient_update'),
    path('recipients/delete/<int:pk>/', views.recipient_delete, name='recipient_delete'),



    # Hospital URLs
    path('hospitals/', views.hospital_list, name='hospital_list'),
    # path('hospitals/create/', views.hospital_create, name='hospital_create'),
    path('hospitals/update/<int:pk>/', views.hospital_update, name='hospital_update'),
    path('hospitals/delete/<int:pk>/', views.hospital_delete, name='hospital_delete'),



    path('recipients/match/<int:pk>/', views.find_matches, name='find_matches'),



    


]
