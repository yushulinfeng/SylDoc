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
    # 管理员相关
    url(r'^SylDoc/manager/$', views.manager),
    url(r'^SylDoc/managerLogin/$', views.managerLogin),
    url(r'^SylDoc/managerAll/$', views.managerAll),
    url(r'^SylDoc/managerAdd/$', views.managerAdd),
    url(r'^SylDoc/managerAlter/$', views.managerAlter),
    url(r'^SylDoc/managerDel/$', views.managerDel),

]
