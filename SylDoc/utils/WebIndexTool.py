#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''首页'''
# 仅允许查，增删，禁止改

from SylDoc.models import WebIndex

# 获取首页推送的书籍列表
def pushList():  # 这个还需要进一步处理，需要与书籍ID统一，后期需要完善
    return WebIndex.objects.filter(type=1)

# 增加或者删除推送书籍
def pushAlter(bid, note="", dele=False):
    note = "" if note == None else note  # python中的三元表达式写法
    try:
        if(dele):  # 删除
            return WebIndex.objects.filter(type=1, bid=bid).delete()  # 返回影响的行数
        else:
            return  WebIndex(bid=bid, note=note, type=1).save()
    except:
        return 0




