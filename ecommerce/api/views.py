from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, WishlistSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Products, Cart, Wishlist
from django.contrib.auth.models import User
import json

from django.http import JsonResponse, HttpResponse, response
@api_view(['GET'])
def categoryshow(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productshow(request,category):
    product = Products.objects.filter(category__name = category)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productdetail(request, id):
    product = Products.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def allproduct(request):
    product = Products.objects.filter(istrending = 1)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addtocart(request):
    if request.method == 'POST':
        data = json.load(request)
        user = data['user']
        product_id = data['product_id']
        qty = data['qty']
        check = Products.objects.get(id = product_id)
        username = User.objects.get(id=user)
        if check:
            if Cart.objects.filter(user=user, product=product_id).exists():
                return JsonResponse({'status':'Product already added'}, safe=False)
            else:
               cart = Cart.objects.create(user=username, product=check, quantity=qty)
               cart.save()
               return JsonResponse({'status':'Added succesfully'}, safe=False)
        else:
            return JsonResponse({'status':'Product is unavailabel'}, safe=False)
    else:
       
        return JsonResponse({'status':f"invalid access"}, safe=False)
    
@api_view(['GET'])
def cartview(request, user):
    cart = Cart.objects.filter(user=user)
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data)
            
@csrf_exempt
def cartdelete(request):
    if request.method == 'POST':
        data = json.load(request)
        user = data['user']
        product_id = data['product_id']
        cart = Cart.objects.get(user=user, product=product_id)
        cart.delete()
        return JsonResponse({'status':'Product removed from the Cart'}, safe=False)
    else:
        return JsonResponse({'status':'Invalid Access!'}, safe=False)
    
@api_view(['POST'])
def addtowish(request):
    if request.method == 'POST':
        data = json.load(request)
        username = data['user']
        product_id = data['product_id']
        check = Products.objects.get(id=product_id)
        user = User.objects.get(id=username)
        if check:
            if Wishlist.objects.filter(user=username, product=product_id).exists():
                return JsonResponse({'status':'Product already added'}, safe=False)
            else:
                wish = Wishlist.objects.create(user=user, product_id=product_id, isliked=True)
                wish.save()
                checking = Wishlist.objects.get(user=user, product=product_id)
                context = {
                    'status':'Product successfully added',
                    'isliked': f"{checking.isliked}"
                }
                return JsonResponse(context, safe=False)
        else:
            return JsonResponse({'status':'Product doesn"t exist'}, safe=False)
    else:
        return JsonResponse({'status':'Invalid Access!'}, safe=False)

@api_view(['GET'])
def wishlistview(request, user):
    wish = Wishlist.objects.filter(user=user)
    serializer = WishlistSerializer(wish, many=True)
    return Response(serializer.data)

@csrf_exempt
def removewish(request):
    if request.method == 'POST':
        data = json.load(request)
        user = data['username']
        product_id = data['product_id']
        cart = Wishlist.objects.get(user=user, product=product_id)
        cart.delete()
        return JsonResponse({'status':'Product removed from the Wishlist'}, safe=False)
    else:
        return JsonResponse({'status':'Invalid Access!'}, safe=False)
    
@api_view(['POST'])
def isliked(request):
    if request.method == 'POST':
        data = json.load(request)
        username = data['user']
        product_id = data['product_id']
        if Wishlist.objects.filter(user=username, product=product_id).exists():
            return JsonResponse({'status':True}, safe=False)
        else:
            return JsonResponse({'status':False}, safe=False)
    else:
        return JsonResponse({'status':'INVALID ACCESS'}, safe=False)