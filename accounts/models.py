# accounts/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    #checkbox 생기는 부분
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
    

