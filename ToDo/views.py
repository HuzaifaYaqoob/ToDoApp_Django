from functools import partial
from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView




from .models import Todo
from .serializers import TodoSerializers
from ToDo import serializers

# Create your views here.


class Todos(APIView):

    def get(self, request):
            
        all_todos = Todo.objects.filter(user=request.user )
        serialized_data = TodoSerializers(all_todos , many=True).data
        return JsonResponse(
                {
                    'data' : serialized_data
                }
            )

    def post(self, request):
        r_data = request.data
        r_data['user'] = request.user.pk
        print(r_data)
        serialized = TodoSerializers(data=r_data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                {
                    'details' : 'Todo Successfuly Added'
                }
            )
        else:
            return Response(
                {
                    'details' : 'Invalid Data'
                },
                status = status.HTTP_409_CONFLICT
            )

    def put(self, request):
        try:
            todo_id = request.GET['todo_id']
            todo_item = Todo.objects.get(id = todo_id)
        except:
            return Response(
                {
                    'details' : 'Todo ID Query Missing'
                },
                status = status.HTTP_404_NOT_FOUND
            )
        else:
            data = request.data

            serialized = TodoSerializers(todo_item , data=data , partial=True)
            if serialized.is_valid():
                serialized.save()
                return Response(
                    {
                        'details' : 'Successfully saved'
                    }
                )

            return Response(
                {
                    'details' : 'Invalid Data'
                }
            )

    def delete(self, request):
        try:
            todo_id = request.GET['todo_id']
            todo_item = Todo.objects.get(id = todo_id)
        except:
            return Response(
                {
                    'details' : 'Todo ID Query Missing'
                },
                status = status.HTTP_404_NOT_FOUND
            )
        else:
            todo_item.delete()
            return Response(
                {
                    'details' : 'Successfully Deleted'
                }
            )