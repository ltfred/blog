from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from utils.models import BaseModel


class User(AbstractUser):
    """用户信息模型类"""
    phone = models.CharField(max_length=20, blank=True, verbose_name='电话')
    avatar_url = models.CharField(max_length=200, blank=True, verbose_name='头像路径')
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username