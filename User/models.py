from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(null=True,upload_to='profiles/',blank=True,default="profiles/default.png")
    Name = models.CharField(max_length=20)
    Email =  models.EmailField(null=True)
    Date_of_Birth = models.DateField(null=True)
    PhoneNumber= models.CharField(max_length=15,null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
        ("other","Other")
    ]
    Gender =  models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    Blood_Group = models.ForeignKey("Blood",on_delete=models.CASCADE,related_name="blood",null=True)
    Division = models.ForeignKey("division",on_delete=models.CASCADE,related_name="division",null=True )  
    District = models.ForeignKey("District",on_delete=models.CASCADE,related_name="district" ,null=True)
    Area = models.CharField(max_length= 20,null=True) 
    Postal_Code = models.IntegerField(null=True) 

    def __str__(self):
        return f"Name :{self.Name}--Email : {self.Email}--Division: {self.Division}--Gender Group:{self.Gender}"

class Blood(models.Model):
    Blood_Group=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.Blood_Group}"

class District(models.Model):
    District_Name=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.District_Name}"

class division(models.Model):
    Division_Name=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.Division_Name}"



