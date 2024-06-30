from django.contrib import admin
from .models import Category, Products, Cart, Wishlist

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Wishlist)