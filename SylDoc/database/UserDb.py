#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户类'''

from __future__ import unicode_literals
from django.db import models

# 用户表，存储用户名与密码
class User(models.Model):
    userid = models.AutoField(primary_key=True)  # int，不用username因为其比较乱
    username = models.CharField(max_length=255, unique=True)
    userpass = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.username

# 用户信息表，存储用户信息
class UserInfo(models.Model):
    userid = models.IntegerField()  # 手动对应User表，暂时不用外码关联
    nickname = models.CharField(max_length=255)  # 昵称
    exp = models.IntegerField()  # 经验值
    rank = models.IntegerField()  # 等级
    gold = models.IntegerField()  # 金币数
    logindate = models.DateField()  # 登录日期，用于当日首次登录判断
    # 后期拓展，暂时不处理
    iconpath = models.CharField(max_length=255)  # 头像地址
    gender = models.IntegerField()  # 性别，1-man，0-woman
    usersign = models.CharField(max_length=255)  # 个性签名
    expend = models.CharField(max_length=255)  # 拓展，json存储
    
    def __unicode__(self):
        return self.userid
    
