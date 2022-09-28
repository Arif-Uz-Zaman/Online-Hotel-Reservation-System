from django.forms import ModelForm
from django import forms

from .models import Hotel
 
# create a ModelForm
class addhotel(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Hotel
        
        fields = "__all__"
        widgets={
            # 'images':forms.ImageField(attrs={'class':'form-control','required':'False'}),
            'hotel_name':forms.TextInput(attrs={'class':'form-control','required':'True','placeholder':"Hotel Name"}),
            'hotel_price':forms.TextInput(attrs={'class':'form-control','required':'True','placeholder':""}),
            'description':forms.Textarea(attrs={'class':'form-control','required':'True'}),
            'amenities':forms.SelectMultiple(attrs={'class':'form-control','required':'True',"multiple":True}),
            'room_count':forms.TextInput(attrs={'class':'form-control','required':'True'}),
            'Division':forms.TextInput(attrs={'class':'form-control','required':'True'}),
            'District':forms.TextInput(attrs={'class':'form-control','required':'True'}),
        }


    