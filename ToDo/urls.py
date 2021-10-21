

from django.urls import path
from . import views

urlpatterns =[
    path('' , views.Todos.as_view() , name='TodoList')
]