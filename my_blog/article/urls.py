from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^list/$', views.ArticleListView.as_view(), name='article_list'),
]