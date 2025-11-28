from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, default="")
    desc = models.TextField()
    pub_date = models.DateField()
    category = models.CharField(max_length=1000, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    desc_preview = models.CharField(max_length=200,default="")
    def __str__(self):
        return f"{self.product_name} - ₹{self.price}"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    name = models.CharField(max_length=90)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_id} by {self.name}"


class OrderUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    update_desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for Order #{self.order.id} on {self.timestamp.strftime('%d-%b-%Y %H:%M')}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=0)
    review_text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Guest'} - {self.rating}★"