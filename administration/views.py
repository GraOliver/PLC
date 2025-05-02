from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import View
from .forms import LoginForm,UserCreationForm
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
            messages.info(request,"Identifiant ou mot de passe incorecte")
            pass
        
        return render(request,self.template)

class UserCreationView(View):
    """Cette fonction est pour la création d'un nouveau utilisateur

    Args:
        View (_type_): _description_

    Returns:
        _type_: _description_
    """
    class_get_element =UserCreationForm
    templates ="Accounts/register.html"
    
    def get(self,request):
        form =self.class_get_element()
        return render(request,self.templates,{"form":form})
    
    def post(self,request):
        form =self.class_get_element(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Accounts:login_user")
        return render(request,self.templates,{"form":form})
    

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('administration:login')