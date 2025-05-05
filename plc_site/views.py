from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth import login,logout,aauthenticate
from django.contrib import messages
from django.views.generic import View
from .models import Photo,Carousel,Activite,Produit,Team,Intervation,Commentaire,Service
from .forms import PhotoForm, ActivityForm,CarouselForm,PersonnelForm,ServiceForm,ProduitForm
from django.contrib.auth.decorators import login_required
import random
# Create your views here.
class Blog (View):
    template ="plc_site/index.html"
    try :
        produit1 =Produit.objects.get(pk =random.randint(0,100))
        
    except :
        # produit1 =Produit.objects.get(pk=1)
        pass
    context= {
        'carousel' : Carousel.objects.all(),
        'commets' : Commentaire.objects.order_by('?')[:4],
        
        # 'produit' :produit1,
        'activity': Activite.objects.order_by('?')[:4],
        'team' :Team.objects.order_by('?')[:4],
        
        'type1' : Produit.objects.filter(cathegorie='pave')[:2],
        'type2' : Produit.objects.filter(cathegorie='block')[:2],
        'type3' : Produit.objects.filter(cathegorie='meuble')[:1],
        'type4' : Produit.objects.filter(cathegorie='architecture')[:1]
    }
    
    def get(self,request):
        return render(request,self.template,self.context)   
    def post(self,request):
        
        if 'commet' in request.POST :
            name =request.POST.get("name")
            phone =request.POST.get("phone")
            email=request.POST.get("email")
            message=request.POST.get("message")
            
            if name and phone and email and message :
                Intervation(identity=name,phone=phone,email=email,commet=message).save()
                return redirect("plc_site:index")
            else :
                return render(request,self.template,{'erreur' : "il y a un probleme"})
                   
class Activity(LoginRequiredMixin, ListView):
    template ="plc_site/description.html"
    
    context ={
        'activity' : Activite.objects.order_by('?')[:4]
        
    }
    def get(self,request) :
        return render(request,self.template,self.context)
    def post(self,request):
        pass

class Services(LoginRequiredMixin, ListView):
    template ="plc_site/services.html"
    context ={
        'services': Service.objects.order_by('?')[:4]
    }
    def get (self, request):
        return render(request,self.template,self.context)
    
# Partie administration
       
class AdminBlog(LoginRequiredMixin, ListView):
    template ="plc_site/administration/blog.html"
    context ={
        'form_activity':ActivityForm(),
        'photo_form':PhotoForm(),
        'activity' : Activite.objects.all()
    }
    def get(self,request):
        return render(request,self.template,self.context)
    
    def post(self,request):
        activity =ActivityForm(request.POST)
        photo = PhotoForm(request.POST,request.FILES)
        
        
        if 'enregistrer' in request.POST :
            if all([activity.is_valid(),photo.is_valid()]):
                photo_file =photo.save(commit=False)
                photo_file.uploader =request.user
                photo_file.save()
                
                activity_file =activity.save(commit=False)
                activity_file.photo =photo_file
                activity_file.save()
                
                return redirect("plc_site:admin")
            else :
                return render(request,self.template,self.context)
class SupAdminBlog (LoginRequiredMixin, ListView):
    def get (self,request,id,id_photo):
        article = get_object_or_404(Activite,id=id)
        article.delete()
        photo =get_object_or_404(Photo,id =id_photo)
        photo.delete()
        
        return redirect('plc_site:admin')


class CarouselView(LoginRequiredMixin, ListView):
    template ="plc_site/administration/carousel.html"
    context ={
        'carousel_form' : CarouselForm(),
        'photo_form':PhotoForm(),
        'activite' : Carousel.objects.all()
    }
    
    def get(self,request):
        return render(request,self.template,self.context)
    
    def post(self,request):
        carousel_form =CarouselForm(request.POST)
        photo_form =PhotoForm(request.POST,request.FILES)
        
        if 'enregistrer' in request.POST :
            if all([carousel_form.is_valid(), photo_form.is_valid()]):
                photo =photo_form.save(commit=False)
                photo.uploader =request.user
                photo.save()
                
                carousel =carousel_form.save(commit=False)
                carousel.photo =photo
                carousel.save()
                
                return redirect('plc_site:admin')
            else :
                return render(request,self.template,self.context)
    

class PersonneView(LoginRequiredMixin, ListView):
    template ="plc_site/administration/personnel.html"
    context ={
        'personnel_form' : PersonnelForm(),
        'photo_form':PhotoForm(),
        'activity': Team.objects.all()
    }
    
    def get(self,request):
        return render(request,self.template,self.context)
    
    def post(self,request):
        personnel_form =PersonnelForm(request.POST)
        photo_form =PhotoForm(request.POST,request.FILES)
        
        if 'enregistrer' in request.POST :
            if all([personnel_form.is_valid(), photo_form.is_valid()]):
                photo =photo_form.save(commit=False)
                photo.uploader =request.user
                photo.save()
                
                personnel =personnel_form.save(commit=False)
                personnel.photo =photo
                personnel.save()
                
                return redirect('plc_site:personnel_view')
            else :
                return render(request,self.template,self.context)

class ProduitView(LoginRequiredMixin, ListView):
    template ="plc_site/administration/produit.html"
    context ={
        'produit_form' : ProduitForm(),
        'photo_form':PhotoForm(),
        'activity' : Produit.objects.all()
    }
    
    def get(self,request):
        return render(request,self.template,self.context)
    
    def post(self,request):
        produit_form =ProduitForm(request.POST)
        photo_form =PhotoForm(request.POST,request.FILES)
        
        if 'enregistrer' in request.POST :
            if all([produit_form.is_valid(), photo_form.is_valid()]):
                photo =photo_form.save(commit=False)
                photo.uploader =request.user
                photo.save()
                
                produit =produit_form.save(commit=False)
                produit.photo =photo
                produit.save()
                
                return redirect('plc_site:produit_view')
            else :
                return render(request,self.template,self.context)

class ServiceView(LoginRequiredMixin, ListView):
    template ="plc_site/administration/services.html"
    context ={
        'service_form' : ServiceForm(),
        'photo_form':PhotoForm(),
        'services' : Service.objects.all()
    }
    
    def get(self,request):
        return render(request,self.template,self.context)
        
    def post(self, request):
        service_form =ServiceForm(request.POST)
        photo_form =PhotoForm(request.POST,request.FILES)
        
        if 'enregistrer' in request.POST :
            if all([service_form.is_valid(), photo_form.is_valid()]):
                photo =photo_form.save(commit=False)
                photo.uploader =request.user
                photo.save()
                
                service =service_form.save(commit=False)
                service.photo =photo
                service.save()
                
                return redirect('plc_site:services_view')
            else :
                return render(request,self.template,self.context)
 

