from django.shortcuts import render,redirect
from django.http import HttpResponse
from hotel.models import (Amenities, Hotel)
from .models import contactus
from django.contrib import messages

from django.db.models import Q
# Create your views here.

def index(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()

    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)
    
    if search:
        hotels_objs = hotels_objs.filter(
            Q(District__icontains = search) |
            Q(hotel_name__icontains = search) )
        context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs 
        , 'search' : search , 'amenities' : amenities}
        


    if len(amenities):
        hotels_objs = hotels_objs.filter(amenities__amenity_name__in = amenities).distinct()
        context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs 
        , 'search' : search , 'amenities' : amenities}
        

    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs 
    , 'search' : search , 'amenities' : amenities}


    
    
    return render(request, "OHRS_App/templates/index.html",context)


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        desc=request.POST.get('desc')
        contactus.objects.create(name=name , Email = email , description=desc)
        messages.success(request,'Message sent successfully')
        return redirect('contact')

    return render(request, "OHRS_App/templates/aboutus.html")

def cust_message(request):
    contact=contactus.objects.all()
    context={
         "contacts":contact,
    }
    return render(request, "OHRS_App/templates/Cmessage.html",context)