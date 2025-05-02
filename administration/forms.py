from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

#Authentification
class LoginForm(AuthenticationForm):
    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        
    class Meta :
        fields =['username']

class UserCreationForm(UserCreationForm):
    class Meta :
        models = User

