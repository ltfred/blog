import markdown
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


class ArticleDetailView(View):
    """文章详情"""

    def get(self, request, article_id):

        try:
            article = ArticlePost.objects.get(id=article_id)
        except:
            return http.HttpResponse('数据库错误')

        # 将markdown语法渲染成html样式
        article.body = markdown.markdown(article.body,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             # 语法高亮扩展
                                             'markdown.extensions.codehilite',
                                         ])

        context = {'article': article}

        return render(request, 'article/detail.html', context)
