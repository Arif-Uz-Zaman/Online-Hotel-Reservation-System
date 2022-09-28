from django.db import models

# Create your models here.
class contactus(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)
    Email =  models.EmailField(null=True)
    description = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name
