from django.conf.urls import url

from userprofile import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # 退出登录
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    # 注册
    url(r'^register/$', views.UserRegisterView.as_view(), name='register'),
    # 重置密码
    url(r'^reset/$', views.ResetPassword.as_view(), name='reset_password'),
    # 个人信息修改
    url(r'^edit/$', views.UserProfileEditView.as_view(), name='edit')

]