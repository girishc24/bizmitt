from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('companylogin/', views.companylogin, name='companylogin'),
    path('<str:company_name>/dashboard/', views.companydashboard, name='companydashboard'),
    path('<str:company_name>/addemployee/', views.addemployee, name='addemployee'),
    path('<str:company_name>/employee/', views.employee, name='employee'),
    path('<str:company_name>/department/', views.department, name='department'),
    
]