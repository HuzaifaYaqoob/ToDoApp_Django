

from django.urls import path , include


urlpatterns = [
    path('todo/' , include('ToDo.urls') , name='ToDo API' ),
    path('auth/' , include('Authentication.urls')  , name='Authentication' ),
]