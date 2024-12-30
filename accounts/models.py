from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Customer(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):         
        return self.name


class Category(models.Model):    
    Categoryname = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):         
        return self.Categoryname
 