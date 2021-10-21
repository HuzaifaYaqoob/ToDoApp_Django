

from .models import Todo
from rest_framework import serializers

from Authentication.serializers import UserSerializers


class TodoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'