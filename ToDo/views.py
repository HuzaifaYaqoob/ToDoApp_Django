from functools import partial
import json
from typing import final
from django.db import connections
from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework import exceptions, status
from rest_framework.response import Response

from rest_framework.views import APIView




from .models import Todo
from .serializers import TodoSerializers

# Create your views here.


class Todos(APIView):

    def get(self, request):
        all_todos = Todo.objects.filter(user=request.user )[::-1]
        try:
            limit = request.GET.get('_limit')
            limit = int(limit)
        except:
            print('Could not get _limits')
            serialized_data = TodoSerializers(all_todos , many=True).data
            print(len(serialized_data))
            return JsonResponse(
                    {
                        'status':'Success',
                        'status_code' : 200,
                        'data' : serialized_data,
                        'total_length' : len(all_todos)
                    }
                )
        else:
            print(limit)
            serialized_data = TodoSerializers(all_todos[0:limit] , many=True).data
            print(len(serialized_data))
            return JsonResponse(
                    {
                        'status':'Success',
                        'status_code' : 200,
                        'data' : serialized_data,
                        'total_length' : len(all_todos)
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
                    'status' : 'Success',
                    'status_code' : 200,
                    'details' : 'Todo Successfuly Added'
                }
            )
        else:
            return Response(
                {
                    'status' : 'Error',
                    'status_code' : 409,
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
                        'status' : 'Success',
                        'status_code' : 200,
                        'details' : 'Successfully saved'
                    }
                )

            return Response(
                {
                    'status' : 'Error',
                    'status_code' : 409,
                    'details' : 'Invalid Data'
                },
                status=status.HTTP_409_CONFLICT
            )

    def delete(self, request):
        try:
            todo_id = request.GET['todo_id']
            todo_item = Todo.objects.get(id = todo_id)
        except:
            return Response(
                {   
                    'status' : 'Error',
                    'status_code' : 404,
                    'details' : 'Todo ID Query Missing',
                },
                status = status.HTTP_404_NOT_FOUND
            )
        else:
            todo_item.delete()
            return Response(
                {
                    'status' : 'Error',
                    'status_code' : 200,
                    'details' : 'Successfully Deleted'
                }
            )