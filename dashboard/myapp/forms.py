from django import forms
from myapp.models import Bord,Usermodel


class MyForm(forms.ModelForm):
    class Meta:
        model = Bord
        fields = ['title']
        

class HomeForm(forms.ModelForm):
    class Meta:
        model = Bord
        fields = ['title','description','duedate','priority']
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields ='__all__'
        
        
class LogInForm(forms.Form):
    username= forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __str__(self):
        return self.username
    

    
# class Dropdownform(forms.Form):
#     li=(('High','High'),('Medium','Medium'),('Low','Low'))
#     dropfield = forms.ChoiceField(choices=li)
