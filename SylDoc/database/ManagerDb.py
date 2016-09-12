#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''管理员相关类'''

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import default

# 管理员表
class WebManager(models.Model):
    username = models.CharField(max_length=255)  # 这个就不用显式ID了
    userpass = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, default='')  # 备用，后期提升管理体验
    usertype = models.IntegerField()
    
    def __unicode__(self):
        return self.username

# 首页管理表
class WebIndex(models.Model):
    bid = models.IntegerField()  # 书籍ID，暂不考虑越界
    note = models.CharField(max_length=255)  # 书籍描述，备用（因为首页一般展示书名）
    type = models.IntegerField()  # 类型，暂时仅1种。1-推荐。
    
    def __unicode__(self):
        return self.username

# 金币管理表（行信息固定表，誉代码关联）
class WebMoney(models.Model):
    type = models.IntegerField()  # 类型，固定。1-注册，2-登录，3-上传，4-检索浏览
    count = models.IntegerField()  # 金币数量
    note = models.CharField(max_length=255)  # 说明，固定。
    
    def __unicode__(self):
        return self.username
