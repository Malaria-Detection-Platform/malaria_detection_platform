from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, )
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    role = models.CharField(max_length=30, default="N/A")
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    RESPONSE_FIELD = ['username']

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
