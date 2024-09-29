from django import forms 
class StudentsRegis(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'form-control'}))
    email = forms.EmailField()
