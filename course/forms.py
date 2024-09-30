from django import forms 
class StudentsRegis(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class StudentsRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile= forms.IntegerField()
   




# widget=forms.TextInput(attrs={'id':'form-control'})