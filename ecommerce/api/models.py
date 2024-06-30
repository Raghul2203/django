from django.db import models
from django.contrib.auth.models import User
import datetime
import os
def getFileName(request, file):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_file = '%s%s' %(current_time, file)
    return os.path.join('images', new_file)
    

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to=getFileName)
    description = models.TextField(max_length=300, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Category"

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName)
    description = models.TextField(max_length=300, null=False, blank=False)
    seller = models.CharField(max_length=50, null=False, blank=False)
    original_price = models.IntegerField(blank=False, null=False)
    selling_price = models.IntegerField(blank=False, null=False)
    offer = models.IntegerField(blank=False, null=False)
    instock = models.IntegerField(blank=False, null=False)
    ratings = models.CharField(max_length=5, null=False, blank=False)
    istrending = models.BooleanField(default=False, help_text='0-hidden, 1-show')
    isavailable = models.BooleanField(default=False, help_text='0-hiddent, 1-show')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Product"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def totalprice(self):
        total = self.quantity * self.product.selling_price
        return total
    class Meta:
        verbose_name_plural = "Cart"
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    isliked = models.BooleanField(default=False, help_text='0-hidden 1-show')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Wishlist"