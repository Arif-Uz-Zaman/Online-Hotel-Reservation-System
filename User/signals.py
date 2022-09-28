from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import profile

# @receiver(post_save, sender=profile)
def createProfile(sender,instance,created,**kawrgs):
    if created:
        user=instance
        Profile=profile.objects.create(
            user=user,
            Name=user.first_name,
            Email=user.email, 
        )



    
def deleteUser(sender,instance,**kawrgs):
    user=instance.user
    user.delete()


def updateUser(sender,instance,created,**kwargs):
    profile  =instance
    user=profile.user

    if created == False:
        user.Name=profile.Name
        user.profile_img=profile.profile_img
        user.Email=profile.Email
        user.Date_of_Birth=profile.Date_of_Birth
        user.PhoneNumber=profile.PhoneNumber
        user.Gender=profile.Gender
        user.Blood_Group=profile.Blood_Group
        user.Division=profile.Division
        user.District=profile.District
        user.Area=profile.Area
        user.Postal_Code=profile.Postal_Code
        user.save()




    



post_save.connect (createProfile,sender=User)
post_save.connect(updateUser,sender=profile)
post_delete.connect(deleteUser,sender=profile)
