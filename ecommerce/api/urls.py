from django.urls import path
from .views import *
app_name = 'api'
urlpatterns = [
    path('category/', categoryshow, name='category'),
    path('products/<category>/', productshow, name='products'),
    path('product/<id>/', productdetail, name='product'),
    path('addtocart/', addtocart, name='addtocart'),
    path('cart/<user>/', cartview, name='cartview'),
    path('removecart/', cartdelete, name='removecart'),
    path('addtowish/', addtowish, name='addtowish'),
    path('wishlist/<user>/', wishlistview, name='wishlist'),
    path('allproduct/', allproduct, name='allproduct'),
    path('isliked/', isliked, name='isliked'),
    path('removewish/', removewish, name='removewish')
]
