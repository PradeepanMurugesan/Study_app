from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  
    path('login/', views.login, name='login'),  
    path('logout/', views.logout, name='logout'),  
    path('main/', views.main_view, name='main_view'),  
    path('add_study/', views.add_study, name='add_study'),  
    path('view_study/<int:pk>/', views.view_study, name='view_study'),  
    path('edit_study/<int:pk>/', views.edit_study, name='edit_study'),  
    path('delete_study/<int:pk>/', views.delete_study, name='delete_study'),  
]
