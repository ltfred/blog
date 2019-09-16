from django.conf.urls import url

from article import views

urlpatterns = [
    # 所有文章
    url(r'^list/$', views.ArticleListView.as_view(), name='article_list'),
    # 文章详情
    url(r'^detail/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail')
]