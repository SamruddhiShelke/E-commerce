from django.contrib import admin
#Password: SVS@svs79
# Register your models here.
# shop/admin.py
from .models import Order,Contact,OrderUpdate
from . models import Product 
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(OrderUpdate)