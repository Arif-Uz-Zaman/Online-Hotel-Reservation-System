
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse

from .models import (Amenities, Hotel, HotelBooking)
from django.db.models import Q
from .forms import addhotel
from django.contrib.auth.decorators import login_required


def check_booking(start_date  , end_date ,uid , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True
    
def Room(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)
    if sort_by:
        if sort_by == 'ASC':
            hotels_objs = hotels_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotels_objs = hotels_objs.order_by('-hotel_price')

    if search:
        hotels_objs = hotels_objs.filter(
            Q(District__icontains = search) |
            Q(hotel_name__icontains = search) )


    if len(amenities):
        hotels_objs = hotels_objs.filter(amenities__amenity_name__in = amenities).distinct()



    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by 
    , 'search' : search , 'amenities' : amenities}
    return render(request , 'room.html' ,context)



def hotel_detail(request,uid):
    hotel_obj = Hotel.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        Payment_type=request.POST.get('Payment-type')
        hotel = Hotel.objects.get(uid = uid)
        if not check_booking(checkin ,checkout  , uid , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = Payment_type)
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

        
    
    return render(request , 'hotel_detail.html' ,{
        'hotels_obj' :hotel_obj
    })




def Addhotel(request):
    context ={}
 
    # create object of form
    form1 = addhotel(request.POST , request.FILES )
    # if request.method=="POST":
    # check if form data is valid
    
    if form1.is_valid():
        # save the form data to model
            form1.save()
            messages.success(request,'Succecfully Added')
            return redirect('add room')
    
    
    context['form']= form1
    return render(request, "addhotel.html", context)


@login_required(login_url='login')
def mybookings(request):
    User=request.user
    Hotel_Booking=HotelBooking.objects.filter(user=User)
    context={
         "HotelBooking":Hotel_Booking,
    }
    if 'hotel' in request.GET:
        hotel = request.GET['hotel']
        HotelBooking.objects.filter(hotel__hotel_name= hotel).filter(user= User).update(booking_status='Canceled')
        
    
    return render(request,"mybookings.html",context)

def bookinglist(request):
    context={}
    Hotel_Booking=HotelBooking.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        hotelBooking=HotelBooking.objects.filter(hotel__hotel_name = q)
        context={
         "HotelBooking":hotelBooking
        }
    

     
    return render(request,"bookinglist.html",context)