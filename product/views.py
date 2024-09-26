from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage(request):
    data = {"User1":[
        {"name":"sherin","loc":"Madurai","Score":100,},
       {"name":"shilpa","loc":"Chennai","Score":90,},
       {"name":"idhaya","loc":"Banglore","Score":80,},
       {"name":"shally","loc":"Chennai","Score":70,},
    ]
    }
    return render(request,'home.html',data)

def aboutpage(request):
    return render(request,'about.html')
#----------------------------------------------------------

class ProductAddView(View):
    def get(self,request):
        data = {"proform":ProductForm}

        return render(request,'productadd.html',data)
    
    def post(self,request):
        new_data = ProductForm(request.POST,request.FILES)

        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
#-----------------------------------------------------------------
class ProductListView(LoginRequiredMixin,View):
    login_url = '/'
    
    def get(self,request):
        data={"prolist":Product.objects.all()}
        
        return render(request,'productlist.html',data)    

#-----------------------------------------------------------------
class ProductUpdateView(View):
    def get(self,request,id):
        selected_row = Product.objects.get(id=id)
        data = {"proform":ProductForm(instance=selected_row)}

        return render(request,'productadd.html',data)
    
    def post(self,request,id):
        selected_row = Product.objects.get(id=id)
        new_data = ProductForm(request.POST,instance=selected_row)

        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
#-----------------------------------------------------------------------

class ProductDeleteView(View):
    def get(self,request,id):
        selected_data = Product.objects.get(id=id)
        selected_data.delete()
        return redirect('/product/productlist/')
    
#-----------------------------------------------------------------------    




        

        

        






        




   
   


