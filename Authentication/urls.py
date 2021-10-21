
from django.urls import path

from . import views

urlpatterns = [
    path('login/' , views.LoginView.as_view() , name='LoginView'),
    path('user/' , views.UserView.as_view() , name='UserView')
]