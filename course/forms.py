from django import forms 
class StudentsRegis(forms.Form):
    name = forms.CharField(min_length = 3)
    email = forms.EmailField()

class StudentsRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
        

    #     if len(valname)< 4 :
    #         raise forms.ValidationError('Name should be more than or equal 4')
        
    #     if len(valemail)<10:
    #          raise forms.ValidationError('Email should be more than or equal 10')
        
       

   
   




# widget=forms.TextInput(attrs={'id':'form-control'})