
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

    
class customer(models.Model): #user
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="customer_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=200)
    phone_no = models.IntegerField(blank=True, null=True)
    address = models.TextField(max_length=300,blank=True,null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        db_table = "customer"
    
class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    brand=models.TextField()
    qty=models.IntegerField()
    price=models.IntegerField()
    category = models.ManyToManyField("Category", blank=True)
    image = models.ImageField(upload_to="product_img",blank=True)
    description = models.CharField(max_length=400,null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.product_name}, {self.brand},{self.qty}, {self.price}"

    class Meta:
        db_table = "Product"

class Category(models.Model):
    Category_name = models.TextField()
    sub_category = models.TextField()
    
    def __str__(self):
        return f"{self.Category_name}, {self.sub_category}"

    class Meta:
        db_table = "Category"


class Order(models.Model):
    product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    delivery_add = models.TextField(max_length=200, null=True)
    status = models.CharField(max_length=20,default= 'PENDING')
    def __str__(self):
        return self.name


    
    
class Comment(models.Model): # review
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    


