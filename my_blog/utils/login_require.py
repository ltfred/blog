from django import http
from django.shortcuts import redirect
from django.urls import reverse


def login_required_json(view_func):
    """
    判断用户是否登录的装饰器，并返回 json
    :param view_func: 被装饰的视图函数
    :return: json、view_func
    """

    def wrapper(request, *args, **kwargs):

        # 如果用户未登录，重定向到登录界面
        if not request.user.is_authenticated():
            # return http.HttpResponse('请先登录')
            return redirect(reverse('userprofile:login'))

        else:
            # 如果用户登录，进入到 view_func 中
            return view_func(request, *args, **kwargs)

    return wrapper


class LoginRequiredMixin(object):
    """验证用户是否登陆"""

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required_json(view)
