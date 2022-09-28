from django import contrib
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import  CustomerRegistration


# Create your views here.
def Registration(request):
    forms = CustomerRegistration()
    if request.method == 'POST':
        forms = CustomerRegistration(request.POST)
        if forms.is_valid():
                forms.save()
                print(forms.errors)
                context_details ={
                    'forms' : forms
                }
                #After customer registation customer details display
                messages.success(request,'Succecfully Registered')
                return render(request, 'login/login.html', context_details)
        else:
            messages.error(request,'Form INVALID')
    context = {
                'forms' : forms,
            }
    return render(request,'registration/registration.html', context)

    
def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            if user.email.endswith('@admin.com'):
                return redirect("/home2.html")
            else:
                return redirect("/home.html")
        else:
             messages.error(request,'Wrong User name or Password') 
             return redirect('/login.html')
    else:
        return render(request,"login/login.html")

def userlogout(request):
    logout(request)
    return redirect('index')
   