from django.db import models
from django.conf import settings

# Create your models here.
class Photo(models.Model) :
    image =models.ImageField()
    caption =models.CharField(max_length=128,blank=True)
    uploader =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption

class Carousel(models.Model):
    title =models.CharField(max_length=128)
    description = models.TextField(max_length=300)
    sub_title =models.CharField(max_length=128)
    photo = models.ForeignKey(Photo,null=True,on_delete=models.SET_NULL,blank=True)
    liens =models.URLField(max_length=200,null =True)
    
    def __str__(self):
        return self.title
    
class Produit(models.Model):
    title =models.CharField(max_length=150)
    description =models.TextField(max_length=280)
    photo =models.ForeignKey(Photo, on_delete=models.SET_NULL,null=True,blank=True)
    cathegorie =models.CharField(max_length=150)
    prix =models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Activite(models.Model):
    title=models.CharField( max_length=150)
    description =models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=False)
    photo =models.ForeignKey(Photo, on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
class Team(models.Model):
    name =models.CharField(max_length=350)
    fonction =models.CharField(max_length=150)
    photo =models.ForeignKey(Photo, verbose_name=("Profil"), on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name


class Commentaire(models.Model):
    identity =models.CharField(("noms"), max_length=350)
    phone =models.CharField(("telephone"), max_length=50)
    commet =models.TextField(("commentaire"))
    photo =models.ForeignKey(Photo, verbose_name=("Profil"), on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.identity

class Intervation(models.Model):
    identity =models.CharField(("noms"), max_length=350)
    phone =models.CharField(("telephone"), max_length=50)
    commet =models.TextField(("commentaire"))
    email =models.EmailField(max_length=254)
    
    def __str__(self):
        return self.identity

class Service(models.Model):
    title =models.CharField(('Titre'),max_length=150)
    description =models.TextField(("Detail"))
    photo =models.ForeignKey(Photo, verbose_name=("Photo"), on_delete=models.SET_NULL,null=True)