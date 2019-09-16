import markdown
from django import http
from django.shortcuts import render, redirect
from django.urls import reverse
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


class NewArticle(View):
    """写文章"""

    def get(self, request):
        """返回写文章页面"""
        return render(request, 'article/create.html')

    def post(self, request):
        """新增文章"""

        # 获取参数
        title = request.POST.get('title')
        body = request.POST.get('body')

        # 检验参数
        if not all([title, body]):
            return http.HttpResponse('缺少必传参数')
        # 获取当前用户
        user = request.user

        try:
            ArticlePost.objects.create(title=title, body=body, author=user)

        except:
            return http.HttpResponse('数据库错误')
        # 新增文章后回到列表页
        return redirect(reverse('article:article_list'))


class DeleteArticleView(View):
    """删除文章"""

    def get(self, request, article_id):
        """删除文章"""

        try:
            article = ArticlePost.objects.get(id=article_id)
            article.delete()
        except:
            return http.HttpResponse('数据库错误')
        # 删除后回到文章列表页
        return redirect(reverse('article:article_list'))


class UpdateArticleView(View):
    """修改文章"""

    def get(self, request, article_id):
        """获取原文章"""
        try:
            article = ArticlePost.objects.get(id=article_id)
        except:
            return http.HttpResponse('数据库错误')

        context = {'article': article}

        return render(request, 'article/update.html', context)

    def post(self, request, article_id):
        # 获取参数
        title = request.POST.get('title')
        body = request.POST.get('body')

        # 检验参数
        if not all([title, body]):
            return http.HttpResponse('缺少必传参数')
        # 获取当前用户
        user = request.user

        try:
            article = ArticlePost.objects.get(id=article_id)
            article.title = title
            article.body = body
            article.save()

        except:
            return http.HttpResponse('数据库错误')
        # 新增文章后回到列表页
        return redirect(reverse('article:article_list'))
