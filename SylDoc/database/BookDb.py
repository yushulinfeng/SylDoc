#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''书籍相关类'''

from __future__ import unicode_literals
from django.db import models
import json

# 书籍表，用于存储与检索
class Book(models.Model):
    bid = models.CharField(max_length=255, primary_key=True)  # 书籍ID, 时间戳_用户ID
    name = models.CharField(max_length=255)  # 书籍名称
    cls = models.CharField(max_length=255, default='')  # 书籍分类（1-4经史子集）（用户选择，不过string更方便）(静态类二级联动)
    subcls = models.CharField(max_length=255, default='')  # 书籍子分类（经10史15子14集5）（用户选择，不过string更方便）
    style = models.CharField(max_length=255, default='')  # 体例，史注等可能有
    dynasty = models.CharField(max_length=255, default='')  # 朝代（用户填写吧）
    describe = models.TextField(default='')  # 描述
    word_title = models.CharField(max_length=255, default='')  # word版标题
    word_describe = models.CharField(max_length=255, default='')  # word版描述
    auth_name = models.CharField(max_length=255, default='')  # 作者名字，多个用英文逗号隔开
    auth_describe = models.TextField(default='')  # 作者描述，多个分段写就行
    check_state = models.IntegerField(default=0)  # 审核状态(0未审核，1通过，-1拒绝（或删除此行）)
    # 书籍存储目录：book-pdf/word/txt形式，以ID命名，不在数据库体现
    # 还有一个书籍封面问题，cover_path
    
    def __unicode__(self):
        return self.bid

    # 将属性和属性值转换成dict 列表生成式  
    def toDict(self):  
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__  
    
    # 封装为json，此方法需要测试一下
    def toJson(self):
        json.dumps(self.toDict(), ensure_ascii=False)  

# 书籍状态表，用于存储书籍的动态状态
class BookState(models.Model):
    bid = models.CharField(max_length=255, primary_key=True)  # 与上面书籍ID对应
    uploader = models.CharField(max_length=255)  # 上传者，对应userid
    upload_time = models.DateTimeField()  # 上传时间
    see = models.IntegerField(default=0)  # 浏览量
    good = models.IntegerField(default=0)  # 赞量
    worse = models.IntegerField(default=0)  # 踩量
    search_see = models.IntegerField(default=0)  # 检索并浏览量，用于金币计算，暂时忽略
    download = models.IntegerField(default=0)  # 下载量，暂时忽略
    
    def __unicode__(self):
        return self.bid

