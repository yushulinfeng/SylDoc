#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views import static
from SylDoc import views
from SylDoc_Server import settings

urlpatterns = [
    url(r'^$', views.homePage),  # 直接主页
    url(r'^SylDoc/$', views.homePage, name='SylDoc'),  # 主页(限制^$，禁止get)
    # 静态页面目录
    url(r'^SylDoc/HomePage/(?P<path>.*)$', static.serve, \
         { 'document_root': settings.STATIC_ROOT }),
]
