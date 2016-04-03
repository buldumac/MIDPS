# -*- coding: utf-8 -*-
"""mydj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from mydjapp.views import index, category, cat_new, cat_del, cat_del_confirm, lot_news, post_sell, post_sell_confirm, search, post_delete, post_delete_confirm

urlpatterns = [
    url(r'^category/(?P<category_id>\d+)/$', category, name='category'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    url(r'^category/new/$', cat_new, name='cat_new'),
    url(r'^lot_products/$', lot_news, name='lot_news'),
    url(r'^category/delete/(?P<category_id>\d+)/$', cat_del, name="cat_del"),
    url(r'^category/delete/(?P<category_id>\d+)/confirmation/$', cat_del_confirm, name="cat_del_confirm"),
    url(r'^post/sell/(?P<post_id>\d+)/$', post_sell, name="post_sell"),
    url(r'^post/sell/(?P<post_id>\d+)/confirmation/$', post_sell_confirm, name="post_sell_confirm"),
    url(r'^post/delete/(?P<post_id>\d+)/$', post_delete, name="post_delete"),
    url(r'^post/delete/(?P<post_id>\d+)/confirmation/$', post_delete_confirm, name="post_delete_confirm"),
    url(r'^login/', "django.contrib.auth.views.login", {"template_name":"login.html"}, name="login"),
    url(r'^logout/', "django.contrib.auth.views.logout",{"template_name":"logout.html"}, name="logout"),
]