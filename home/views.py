from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from hotel.models import (Amenities, Hotel)
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url='login')
def home(request):
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
    return render(request,"home/home.html",context)

@login_required(login_url='login')
def home2(request):
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
    return render(request,"home/home2.html",context)

@login_required(login_url='login')
def aboutus(request):
    return render(request,"About_us.html")
