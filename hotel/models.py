
from django.contrib.auth.models import User
from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name

class Hotel(BaseModel):
    images = models.ImageField(upload_to="hotels/")
    hotel_name= models.CharField(max_length=100,null=True,blank=True)
    hotel_price = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    amenities = models.ManyToManyField(Amenities,blank=True)
    room_count = models.IntegerField(default=10,null=True,blank=True)
    Division= models.CharField(max_length=20,null=True,blank=True)
    District= models.CharField(max_length=20,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.hotel_name}"




class HotelBooking(BaseModel):
    hotel= models.ForeignKey(Hotel  , related_name="hotel_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))
    booking_status= models.CharField(max_length=10,default="Booked")
    def __str__(self):
        return f"{self.hotel} -  -  - {self.user}"
    

