from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class ActivityForm (forms.ModelForm):
    class Meta :
        model = models.Activite
        fields =['title','description','date','photo']
        
        widgets={
            'title':forms.TextInput(attrs={
                'class': 'form-control black',
            }),
            'description':forms.Textarea(attrs={
                'class' : "form-control",
                'row' :4
            }),
            
            'date':forms.DateInput(attrs ={
                'class' : 'form-control',
                'type': 'date'
            })
        }
            
class PhotoForm (forms.ModelForm):
    class Meta :
        model =models.Photo
        fields =['image','caption']
        
        widgets ={
            'caption' :forms.TextInput(attrs ={
                'class' : 'form-control',
                'placeholder' :'titre de la photo'
            }),
            
            'image' :forms.ClearableFileInput(attrs ={
                'class' : 'form-control'
            })
            
            
        }

class CarouselForm(forms.ModelForm):
    class Meta:
        model = models.Carousel
        fields =['title','description','sub_title','liens']
        
        widgets ={
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
            }),
            'sub_title' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            'liens' : forms.TextInput(attrs={
                'class' :'form-control'
                
            }),
            
        }
        pass
    pass

class PersonnelForm(forms.ModelForm):
    class Meta :
        model = models.Team
        fields =['name','fonction']
        
        widgets ={
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            
            'fonction' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
        }
        
class ProduitForm (forms.ModelForm):
    class Meta :
        model = models.Produit
        fields =['title','description','cathegorie','prix']
        
        widgets={
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
            }),
            
            'cathegorie' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            
            'prix' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
        }
        
class CommetForme (forms.ModelForm):
    class Meta :
        model = models.Commentaire
        fields =['identity','commet','phone']
        
        widgets={
            'identity' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            'comment' : forms.Textarea(attrs={
                'class' : 'form-control',
            }),
            
            'phone' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
        }

class ServiceForm(forms.ModelForm):
    class Meta :
        model = models.Service
        fields =['title','description']
        
        widgets ={
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
            }),
        }

class IntervationForm(forms.ModelForm):
    pass 

