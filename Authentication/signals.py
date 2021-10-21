

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save , sender=User)
def Create_AuthToken(sender , instance, created , **kwargs):
    if created:
        user_token = Token.objects.create(user = instance)
