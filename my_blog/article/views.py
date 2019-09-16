from django import http
from django.shortcuts import render


# Create your views here.

def article_list(request):
    return http.HttpResponse('hello word')
