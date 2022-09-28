from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import MinLengthValidator
    
    
#Customer registrarion forms create
class CustomerRegistration(UserCreationForm):
   
    def clean_email(self):
            # Get the email
            email = self.cleaned_data.get('email')

            # Check to see if any users already exist with this email as a username.
            try:
                match = User.objects.get(email=email)
            except User.DoesNotExist:
                # Unable to find a user, this is fine
                return email

            # A user was found with this as a username, raise an error.
            raise forms.ValidationError('This email address is already in use.')
        
    class Meta:
        model = User
        fields = ["first_name","username", "email", "password1", "password2"]
