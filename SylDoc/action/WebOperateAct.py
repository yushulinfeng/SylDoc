#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''事件管理相关，内容与运营'''

from SylDoc.utils.Tools import webResponse
from SylDoc.models import  WebManager

'''
金币奖励修改
send:type,count
resp:1-succ,-1-login,-2-fail
'''
def operateMoneyAlter(request):  
    pass

'''
添加首页数据
send:bid,note,type(目前只有1)
resp:1-succ,-1-login,-2-fail
'''
def operateIndexAdd(request):  
    pass

'''
删除首页数据
send:id
resp:1-succ,-1-login,-2-fail
'''
def operateIndexDel(request):  
    pass

'''
获取金币奖励列表
send:null
resp:json-succ,-1-login,-2-fail
'''
def operateMoneyList(request):  
    pass

'''
获取首页数据列表(暂不考虑分页)
send:null
resp:json-succ,-1-login,-2-fail
'''
def operateIndexList(request):  
    pass

