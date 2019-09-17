import random
import re
from django import http
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from userprofile.models import User
from utils.login_require import LoginRequiredMixin
from utils.mail import send_reset_mail


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


class LogoutView(LoginRequiredMixin, View):
    """退出登录"""
    def get(self, request):
        logout(request)
        return redirect(reverse('article:article_list'))


class UserRegisterView(View):
    """用户注册"""

    def get(self, request):
        """返回注册界面"""
        return render(request, 'userprofile/register.html')

    def post(self, request):
        """注册"""

        # 获取参数
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, email, password, password2]):
            return http.HttpResponse('缺少必传参数')

        if not password == password2:
            return http.HttpResponse('两次密码输入不相同')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        except:
            return http.HttpResponse('注册失败')
        # 状态保持
        login(request, user)
        # 跳转到列表页
        return redirect(reverse('article:article_list'))


class ResetPassword(View):
    """重置用户密码"""

    def get(self, request):
        """返回重置密码界面"""
        return render(request, 'userprofile/reset_password.html')

    def post(self, request):

        email = request.POST.get('email')

        if not email:
            return http.HttpResponse('请输入邮箱')

        if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            return http.HttpResponse('请输入正确的邮箱')

        password = '%06d' % random.randint(0, 999999)

        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
        except:
            return http.HttpResponse('你的邮箱没有注册')

        send_reset_mail(email, password)

        return redirect(reverse('userprofile:login'))


class UserProfileEditView(LoginRequiredMixin, View):
    """个人信息修改"""
    def get(self, request):

        user = request.user

        context = {'user': user}

        return render(request, 'userprofile/edit.html', context=context)