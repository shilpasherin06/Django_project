from django.db import models

class Product(models.Model):
    Brand_name = models.CharField(max_length=200,null=True)

    Model_name = models.CharField(max_length=200,null=True)

    price        = models.IntegerField(default=0)

    gst          = models.FloatField(default=0)

    final_price  = models.IntegerField(default=0)

    picture      = models.ImageField(null=True,upload_to='images/')
    

    def __str__(self):
        return self.Brand_name + " " + self.Model_name