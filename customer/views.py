from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View


def indexpage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')
#-------------------------------------------------------
class CustomerAddView(View):
    def get(self,request):
        data = {"cusform":CustomerForm}

        return render(request,'customeradd.html',data)
    
    def post(self,request):
        new_data = CustomerForm(request.POST)

        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')
#----------------------------------------------------------        
class CustomerListView(View):
    def get(self,request):
        data={"cuslist":Customer.objects.all()}
        return render(request,'customerlist.html',data)
        
#---------------------------------------------------------------  
class CustomerUpdateView(View):
    def get(self,request,id):
        selected_row = Customer.objects.get(id=id)
        data = {"cusform":CustomerForm(instance=selected_row)}

        return render(request,'customeradd.html',data) 
    
    def post(self,request,id):
        selected_row = Customer.objects.get(id=id)
        new_data = CustomerForm(request.POST,instance=selected_row)

        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')
#------------------------------------------------------------------------
class CustomerDeleteView(View):
    def get(self,requst,id):
        selected_data = Customer.objects.get(id=id)
        selected_data.delete()
        return redirect('/customer/customerlist/')
    
#-----------------------------------------------------------------------    




        




        

