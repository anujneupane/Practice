from django import forms 
from django.core import validators
class StudentsRegis(forms.Form):
    name = forms.CharField(min_length = 3)
    email = forms.EmailField()

class StudentsRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField()
   
 
        
       

   
   




