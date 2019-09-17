from django.conf.urls import url

from userprofile import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # 退出登录
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]