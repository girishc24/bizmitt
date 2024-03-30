from django.shortcuts import render
from django.http import HttpResponse



def signup(request):
    #return HttpResponse("Company Register")
    return render(request, 'signup.html')

def companylogin(request):
    return render(request, 'signin.html')