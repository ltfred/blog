from django import http
from django.shortcuts import render


from django.views import View

from article.models import ArticlePost


class ArticleListView(View):
    """所有博客文章"""

    def get(self, request):

        try:
            articles = ArticlePost.objects.all()

        except:
            return http.HttpResponse('数据库错误')

        context = {'articles': articles}

        return render(request, 'article/list.html', context)
