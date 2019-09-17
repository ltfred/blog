from django import http
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from userprofile.models import User


class LoginView(View):
    """用户登录"""

    def get(self, request):
        """返回登录界面"""
        return render(request, 'userprofile/login.html')

    def post(self, request):
        # 获取参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all([username, password]):
            return http.HttpResponse('参数错误')

        try:
            user = User.objects.get(username=username)
        except:
            return http.HttpResponse('用户名或密码错误')
        if not user.check_password(password):
            return http.HttpResponse('用户名或密码错误')

        # 状态保持
        login(request, user)

        return redirect(reverse('article:article_list'))


class LogoutView(View):
    """退出登录"""
    def get(self, request):
        logout(request)
        return redirect(reverse('article:article_list'))