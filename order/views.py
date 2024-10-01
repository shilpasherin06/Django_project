from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#-----------------------------------------------------------------------
class OrderAddView(View):
    def get(self,request):
        data = {"ordform":OrderForm}
        return render(request,'orderadd.html',data)
    
    def post(self,request):
        sp = Product.objects.get(id = request.POST['product_ref'])
        pro_price = float(request.POST['quantity']) * sp.price
        pro_gst = (pro_price * sp.gst)/100
        pro_final_price = pro_price + pro_gst

        new_order = Order(product_ref_id  = request.POST['product_ref'],
              
                          customer_ref_id = request.POST['customer_ref'],
              
                          order_date   = request.POST['order_date'],
              
                          quantity     = request.POST['quantity'],
              
                          price        = pro_price,
              
                          gst          = pro_gst,
              
                          final_price  = pro_final_price,

              )
        new_order.save()

        return redirect('/order/orderlist/')
    
#-------------------------------------------------------------------
class OrderListView(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request):
        data={"ordlist":Order.objects.all()}
        return render(request,'orderlist.html',data)
#----------------------------------------------------------
class OrederUpdateView(View):
    def get(self,request,id):
        selected_row = Order.objects.get(id=id)
        data = {"ordform":OrderForm(instance=selected_row)}

        return render(request,'orderadd.html',data)
    
    def post(self,request,id):
        sp = Product.objects.get(id = request.POST['product_ref'])

        pro_price = float(request.POST['quantity']) * sp.price
        pro_gst = (pro_price * sp.gst)/100
        pro_final_price = pro_price + pro_gst

        updated_row = Order.objects.filter(id=id)

        updated_row.update(product_ref_id  = request.POST['product_ref'],
              
                           customer_ref_id = request.POST['customer_ref'],
              
                           order_date   = request.POST['order_date'],
              
                           quantity     = request.POST['quantity'],
              
                           price        = pro_price,
              
                           gst          = pro_gst,
              
                           final_price  = pro_final_price,)
        return redirect('/order/orderlist/')
#-------------------------------------------------------------------------
class OrderDeleteView(View):
    def get(self,request,id):
        selected_data = Order.objects.get(id=id)
        selected_data.delete()
        return redirect('/order/orderlist/')
#-------------------------------------------------------------------------    












 