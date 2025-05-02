from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

#Authentification
class LoginForm(forms.ModelForm):
    class Meta :
        model =User
        fields =['username','password']
        
        widgets={
            'username' : forms.TextInput(attrs={
                'class':'form-control'
            }),
            'password' : forms.PasswordInput(attrs={
                'class':'form-control'
            })
        }

class UserCreationForm(UserCreationForm):
    class Meta :
        models = User

