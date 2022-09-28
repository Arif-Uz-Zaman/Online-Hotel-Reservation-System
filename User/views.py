from django.shortcuts import redirect, render
# from User.models import profile
from django.contrib import messages
from .models import profile
from django.contrib.auth.decorators import login_required
from .forms import  Customerinfo


# Create your views here.
@login_required(login_url='login')
def editinfo(request):
    profile=request.user.profile
    forms = Customerinfo(instance=profile)
    if request.method=="POST":
         form =Customerinfo(request.POST,request.FILES,instance=profile)
         if form.is_valid():
              form.save()
              return redirect("profile.html")
    context = { 'forms' : forms}
    return render(request,'editinfo/editinfo.html', context)


@login_required(login_url='login')
def userProfile(request):
    profile=request.user.profile
    context={
         "profile":profile
    }
    return render(request,"profile/profile.html",context)