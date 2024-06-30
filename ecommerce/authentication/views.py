from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

@csrf_exempt
def getusername(request):
    if request.method == 'POST':
        data = json.load(request)
        user_id = data['user_id']
        user = User.objects.get(id=user_id)
        return JsonResponse({'user':f"{user}"}, safe=False)
    else:
        return JsonResponse({'status':'user is not allowed'}, safe=False)


    