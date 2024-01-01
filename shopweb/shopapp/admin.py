
from django.contrib import admin
from .models import *

admin.site.register(customer) #user
admin.site.register(Product)#product
admin.site.register(Category)
admin.site.register(Order)#Order
admin.site.register(Comment) #review
