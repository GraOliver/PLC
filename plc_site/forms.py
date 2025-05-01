from django import forms
from . import models

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
                'class' : 'formm-control'
            }),
            
            'image' :forms.ClearableFileInput(attrs ={
                'class' : 'form-control'
            })
            
            
        }
        