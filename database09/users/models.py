from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class User(AbstractUser):
    username = None  # username을 사용 안할 경우
    profile_image=models.TextField()
    name=models.CharField(max_length=10,null=True,blank=True)
    nickname=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
