from django.db import models
from userprofile.models import User
from utils.models import BaseModel


class ArticlePost(BaseModel):
    """博客文章模型类"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    body = models.TextField(verbose_name='文章正文')

    class Meta:
        db_table = 'article'
        verbose_name = '博客文章'
        verbose_name = verbose_name
        ordering = ('-create_time',)

    def __str__(self):

        return self.title
