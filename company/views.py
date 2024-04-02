from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from . models import Company
from django.contrib import messages
from . decorators import group_required

def signup(request):
    if request.method == "POST":
        business= request.POST['business']
        email= request.POST['email']
        password= request.POST['password']
        phoneno= request.POST['phoneno']
        user = User.objects.create_user(username=phoneno, email=email, password=password)
        company_group = Group.objects.get(name='COMPANY')
        user.groups.add(company_group)
        company = Company.objects.create(user=user, business=business, email=email, phoneno=phoneno, password=password)
        return redirect('signup')
    else:
        #return HttpResponse("Company Register")
        return render(request, 'signup.html')

def companylogin(request):
    if request.method == "POST":
        phoneno=request.POST['phoneno']
        password=request.POST['password']
        user = authenticate(request, username=phoneno, password=password)
        if user is not None:
            company_group = Group.objects.get(name='COMPANY')
            if company_group in user.groups.all():
                login(request, user)
                company = Company.objects.get(user=user)
                company_name = company.business
                return redirect('companydashboard', company_name=company_name)
            else:
                messages.error(request, "You are not authorized to access this page.")
                return redirect('companylogin')
        else:
            messages.error(request, "Invalid phone number or password.")
            return redirect('companylogin')
    else:
        return render(request, 'signin.html')
    
@group_required('COMPANY')
def companydashboard(request, company_name):
    if request.user.is_authenticated:
        try:
            company = Company.objects.get(user=request.user) 
            context = {"company": company}
            return render(request, 'index.html', context)
        except Company.DoesNotExist:
            messages.error(request, "Company not found for the logged-in user.")
            return redirect('companylogin')
    else:
        messages.error(request, "Need to login.")
        return redirect('companylogin')
    
@group_required('COMPANY')
def addemployee(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        context = {"company": company}
        return render(request, 'addemployee.html', context)
    else:
        return redirect('companylogin')
    
@group_required('COMPANY')   
def department(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        context = {"company": company}
        return render(request, 'department.html', context)
    else:
        return redirect('companylogin')
    
