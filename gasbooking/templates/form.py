
from gasbookapp.models import *
from django import forms


from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

'''
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']
        '''
class DateInput(forms.DateInput):
    input_type = 'date'


class ConnectionForm(forms.ModelForm):
    class Meta:
        model=Connection
        #widgets={'applieddate':DateInput()}
        exclude = ['applieddate']
        fields = ['name','email','mobilenumber','gender','marriedstatus','adharno','address','applieddate','zipcode']

class BookForm(forms.ModelForm):
    class Meta:
        model=BookGas
       # widgets={'date':DateInput()}
        exclude = ['date']
        fields = ['cylinder_KG','date']


