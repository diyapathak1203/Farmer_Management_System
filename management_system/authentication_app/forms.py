from django import forms   
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class employee_register_form(UserCreationForm):

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(label='Confrim Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    
    
    class Meta:
        model = User
        fields = ["username","email"]

        widgets = {

            'username' : forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'email' : forms.TextInput(attrs={'placeholder':'Email Address'}),
          
        }

class employee_login_form(AuthenticationForm):
    username = forms.CharField(
        label='username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}))

    
  