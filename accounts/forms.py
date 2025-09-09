from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import ApplicationsForEditors

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username' , 'email', 'password1', 'password2']

class UserLoingForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class UserProfileUpdate(forms.ModelForm):
     class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email']
        widgets = {
    'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
              }
        
class EditorApplyForm(forms.ModelForm):
    class Meta:
        model = ApplicationsForEditors
        fields = ['first_name', 'last_name','gender', 'email', 'phone_number', 'n_id', 'educations', 'zip_code', 'city', 'state', 'country']