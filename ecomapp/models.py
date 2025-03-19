from django.db import models
from django.contrib.auth.models import User
#Product table
class Product(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(null=True,blank=True,max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0) 
    image = models.ImageField(upload_to='product_pic/', blank=True, null=True)

    def __str__(self):
        return self.name
    

