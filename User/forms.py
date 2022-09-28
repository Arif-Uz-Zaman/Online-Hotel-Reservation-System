from django import forms
from django.forms import ModelForm
from .models import profile

    
    
#customer registrarion forms create
class Customerinfo(ModelForm):
    class Meta:
        model = profile
        fields = ["profile_img" ,"Name" ,"Email" ,"Date_of_Birth" ,"PhoneNumber" ,"Gender" ,"Blood_Group" ,"Division" ,"District" ,"Area","Postal_Code"]
       
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control','required':'True', 'placeholder':"Full Name"}),
            'Email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'Gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'Date_of_Birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'Blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'Phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'Division' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'District' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'Area' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'PostalCode' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
        }