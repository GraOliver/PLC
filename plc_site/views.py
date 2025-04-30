from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import Photo,Carousel,Activite,Produit,Team,Intervation,Commentaire
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
                   
        

class Activity(View):
    def get(self,request) :
        pass
    def post(self,request):
        pass
