from django.db import models
from product.models import *
from customer.models import *

class Order(models.Model):
    product_ref    = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

    customer_ref   = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)

    order_date     = models.DateTimeField(null=True)

    quantity       = models.IntegerField(default=0)

    price          = models.IntegerField(default=0)

    gst            = models.FloatField(default=0)

    final_price    = models.IntegerField(default=0)

    