from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('companylogin/', views.companylogin, name='companylogin'),
    path('<str:company_name>/dashboard/', views.companydashboard, name='companydashboard'),
    path('<str:company_name>/addemployee/', views.addemployee, name='addemployee'),
    path('<str:company_name>/department/', views.department, name='department'),
    
]