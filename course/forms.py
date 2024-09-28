from django import forms 
class StudentsRegis(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
