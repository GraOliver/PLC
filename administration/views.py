from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import View
from .forms import LoginForm
# Create your views here.
class Login(View):
    template ="administration/login.html"
    context ={
        'login_form' :LoginForm()
    }
    def get(self,request):
        return render(request,self.template,self.context)
    
    def post(self,request):
        user =authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
            )
        
        if user is not None :
            login(request,user)
            return redirect('plc_site:admin')
            
        else :
            # messages.info(request,"Identifiant ou mot de passe incorecte")
            pass
        
        return render(request,self.template)
            
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('administration:login')