from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from hotel.models import (Amenities, Hotel)
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

    if request.method == 'POST':
        msg = request.POST.get('subscribe-email')
        
        subject = 'welcome to OHRS'
        message = f'Hi there, thank you for subscribing OHRS. Now you will get all the discount notification. '
        e_from = settings.EMAIL_HOST_USER
        email =[msg,]
        send_mail(subject,message,e_from,email)
        messages.success(request,'Subscribed Successfully. Please check your email.')
        

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

    if request.method == 'POST':
        msg = request.POST.get('subscribe-email')
        
        subject = 'welcome to OHRS'
        message = f'Hi there, thank you for subscribing OHRS. Now, you will receive all the discount notification through email. '
        e_from = settings.EMAIL_HOST_USER
        email =[msg,]
        send_mail(subject,message,e_from,email)
        messages.success(request,'Subscribed Successfully. Please check your email.')
        

    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs 
    , 'search' : search , 'amenities' : amenities}
    return render(request,"home/home2.html",context)

@login_required(login_url='login')
def aboutus(request):
    return render(request,"About_us.html")
