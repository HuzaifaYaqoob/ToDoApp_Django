from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate


from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status

from .serializers import UserSerializers

# Create your views here.


class UserView(APIView):
    def get(self, request):
        serialized_obj = UserSerializers(request.user)

        return JsonResponse(
            {
                'user' : serialized_obj.data
            }
        )

@permission_classes((AllowAny, ))
class LoginView(APIView):

    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(username = username, password =password)
        if user is not None:
            serialized_obj = UserSerializers(user )
            return JsonResponse(
                {
                    'data' : {
                        'user' : serialized_obj.data
                    }
                }
            )

        return Response(
            {
                'details' : 'Invalid Credentials'
            },
            status = status.HTTP_401_UNAUTHORIZED
        )
        

        
