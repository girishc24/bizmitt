from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . models import Company, Department, Designation, Employee, Tier, Reimbursementlist
from django.contrib import messages
from . decorators import group_required

def signup(request):
    if request.method == "POST":
        business= request.POST['business']
        email= request.POST['email']
        password= request.POST['password']
        gstno= request.POST['gstno']
        user = User.objects.create_user(username=email, email=email, password=password)
        company_group = Group.objects.get(name='COMPANY')
        user.groups.add(company_group)
        company = Company.objects.create(user=user, business=business, email=email, gstno=gstno, password=password)
        return redirect('signup')
    else:
        #return HttpResponse("Company Register")
        return render(request, 'signup.html')

def companylogin(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            company_group = Group.objects.get(name='COMPANY')
            if company_group in user.groups.all():
                login(request, user)
                company = Company.objects.get(user=user)
                company_name = company.business.replace(' ','')
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
            company =company.business.replace(' ','')
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
        
        if request.method == "POST":
            employeename=request.POST["employeename"]
            phoneno_new=request.POST["phoneno"]
            email_new=request.POST["email"]
            officalemail=request.POST["officalemail"]
            department_new=request.POST["department"]
            department_instance = Department.objects.get(id=department_new)
            designation_new=request.POST["designation"]
            designation_instance = Designation.objects.get(id=designation_new)
            tier_new=request.POST["tier"]
            tier_instance = Tier.objects.get(id=tier_new)
            password=request.POST["password"]
            user = User.objects.create_user(username=phoneno_new, email=officalemail, password=password)
            company_group = Group.objects.get(name='EMPLOYEE')
            user.groups.add(company_group)
            company = Employee.objects.create(user=user, cno=company, employeename=employeename, phoneno=phoneno_new, email=email_new, officalemail=officalemail, department=department_instance, designation=designation_instance, tier=tier_instance, password=password)
            return redirect(f'/{company.business}/employee/')
        else:
            department = Department.objects.filter(cno=company)
            designation = Designation.objects.filter(cno=company)
            tier = Tier.objects.filter(cno=company)
            company =company.business.replace(' ','')
            context = {"company": company,  "department":department, "designation":designation, "tier":tier}
            return render(request, 'addemployee.html', context)
    else:
        return redirect('companylogin')
    
@group_required('COMPANY')
def employee(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        employee = Employee.objects.filter(cno=company)
        company =company.business.replace(' ','')
        context = {"company": company, "employee":employee}
        return render(request, 'employee.html', context)
    else:
        return redirect('companylogin')
    
@group_required('COMPANY')   
def department(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            #cno = request.POST['cno']
            department_name = request.POST['department']
            department = Department.objects.create(cno=company, department=department_name)
            company =company.business.replace(' ','')
            
            return redirect(f'/{company}/department/')
        else:
            department = Department.objects.filter(cno=company)
            
            company =company.business.replace(' ','')
            context = {"company": company, "department":department}
            return render(request, 'department.html', context)
    else:
        return redirect('companylogin')

@group_required('COMPANY')   
def editdepartment(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
             department_name = request.POST['department']
             pk = request.POST['dno']
             department = Department.objects.filter(id=pk).update(department=department_name)
             company =company.business.replace(' ','')
             return redirect(f'/{company}/department/')


@group_required('COMPANY')   
def designation(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            #cno = request.POST['cno']
            designation_name = request.POST['designation']
            dno = request.POST['dno']
            department= Department.objects.get(id=dno)
            designation = Designation.objects.create(cno=company, designation=designation_name, dno=department)
            company =company.business.replace(' ','')
            return redirect(f'/{company}/designation/')
        else:
            designation = Designation.objects.filter(cno=company)
            department = Department.objects.filter(cno=company)
            company =company.business.replace(' ','')
            context = {"company": company, "designation":designation, "department":department}
            return render(request, 'designation.html', context)
    else:
        return redirect('companylogin')
    
@group_required('COMPANY')   
def editdesignation(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
             designation_name = request.POST['designation']
             pk = request.POST['dno']
             department = Designation.objects.filter(id=pk).update(designation=designation_name)
             company =company.business.replace(' ','')
             return redirect(f'/{company}/designation/')
        
@group_required('COMPANY')   
def tier(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            #cno = request.POST['cno']
            tier_name = request.POST['tier']
            tier = Tier.objects.create(cno=company, tier=tier_name)
            company =company.business.replace(' ','')
            return redirect(f'/{company}/tier/')
        else:
            tier = Tier.objects.filter(cno=company)
            company =company.business.replace(' ','')
            context = {"company": company, "tier":tier}
            return render(request, 'tier.html', context)
    else:
        return redirect('companylogin')
    
@group_required('COMPANY')   
def edittier(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
             tier = request.POST['tier']
             pk = request.POST['tno']
             tier = Tier.objects.filter(id=pk).update(tier=tier)
             company =company.business.replace(' ','')
             return redirect(f'/{company}/tier/')
    
@group_required('COMPANY')   
def reimbursementlist(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            #cno = request.POST['cno']
            name = request.POST['name']
            tier = Reimbursementlist.objects.create(cno=company, list=name)
            company =company.business.replace(' ','')
            return redirect(f'/{company}/reimbursementlist/')
        else:
            reimbursement = Reimbursementlist.objects.filter(cno=company)
            company =company.business.replace(' ','')
            context = {"company": company, "reimbursement":reimbursement}
            return render(request, 'reimbursementlist.html', context)
    else:
        return redirect('companylogin')

@group_required('COMPANY')   
def editreimbursementlist(request, company_name):
    if request.user.is_authenticated:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
             list_name = request.POST['list']
             pk = request.POST['rno']
             tier = Reimbursementlist.objects.filter(id=pk).update(list=list_name)
             company =company.business.replace(' ','')
             return redirect(f'/{company}/reimbursement/')
    
@group_required('COMPANY')   
def logout_view(request):
    logout(request)
    return redirect('companylogin')

    
