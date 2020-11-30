"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index import index_urls
from login import login_urls
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(index_urls)),
    path('login/', include(login_urls)),
    path('index/', views.index, name='index'),
]
'''
路径转换器
str - 匹配除了 '/' 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
int - 匹配 0 或任何正整数。返回一个 int 。
slug - 匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，building-your-1st-django-site 。
uuid - 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID 实例。
path - 匹配非空字段，包括路径分隔符 '/' 。它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分。
'''
