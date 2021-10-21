from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Todo(models.Model):

    TODO_STATUS = [
        ['ToDo' , 'ToDo'],
        ['Doing' , 'Doing'],
        ['In Progress' , 'In Progress'],
        ['Done' , 'Done'],
        ['Completed' , 'Completed'],
    ]

    user = models.ForeignKey(User, default=None, related_name='user_todos' , on_delete=models.CASCADE)
    title = models.CharField(max_length=200 , default=None)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    status = models.CharField(choices=TODO_STATUS , max_length=15 , default='ToDo')
    starts_date = models.DateField(auto_now=now)
    ends_date = models.DateField()

        


    def __str__(self):
        return self.user.username