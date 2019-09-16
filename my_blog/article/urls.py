from django.conf.urls import url

from article import views

urlpatterns = [
    # 所有文章
    url(r'^list/$', views.ArticleListView.as_view(), name='article_list'),
    # 文章详情
    url(r'^detail/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    # 写文章
    url(r'^create/$', views.NewArticle.as_view(), name='article_create'),
    # 删除文章
    url(r'^delete/(?P<article_id>\d+)/$', views.DeleteArticleView.as_view(), name='article_delete')
]