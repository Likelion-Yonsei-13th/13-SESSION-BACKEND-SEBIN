from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
#username, email, password 는 이미 포함
    nickname = models.CharField(max_length=30, blank=True)
    #소셜로그인 시 필요 : 구글, 네이버 등의 유저정보
    provider = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nickname
