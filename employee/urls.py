from django.urls import path
from . import views

urlpatterns = [
    path('employeelogin/', views.employeesign, name='employeesign'),
  
    
]