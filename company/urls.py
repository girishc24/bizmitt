from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('companylogin/', views.companylogin, name='companylogin'),
    path('dashboard/', views.companydashboard, name='companydashboard'),
    
]