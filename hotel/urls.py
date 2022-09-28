from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('check_booking/' , check_booking),
    path('room', Room , name='Room'),
    path('mybookings.html', mybookings , name='mybookings'),
    path('bookinglist.html', bookinglist , name='bookinglist'),
    path('room.html', Room , name='Room'),
    path('addhotel.html', Addhotel,name='add room'),
    path('addhotel', Addhotel,name='add room'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    # path('login/', login_page , name='login_page'),
    # path('register/', register_page , name='register_page'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()