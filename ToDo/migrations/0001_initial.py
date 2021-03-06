# Generated by Django 3.2.8 on 2021-10-20 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('status', models.CharField(choices=[['ToDo', 'ToDo'], ['Doing', 'Doing'], ['In Progress', 'In Progress'], ['Done', 'Done'], ['Completed', 'Completed']], default='ToDo', max_length=15)),
                ('starts_date', models.DateField(auto_now=True)),
                ('ends_date', models.DateField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_todos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
