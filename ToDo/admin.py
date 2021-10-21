from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'status',
        'starts_date',
        'ends_date',
        'ends_date',
    ]
admin.site.register(Todo , TodoAdmin)