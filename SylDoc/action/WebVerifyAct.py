#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''管理书籍相关，审核与修改'''

from SylDoc.utils.Tools import webResponse
from SylDoc.models import  WebManager

'''
获取需要审核书籍里列表(暂不考虑分页)
send:null
resp:json-succ,-1-login,-2-fail
'''
def verifyList(request):  
    pass

'''
审核书籍，设定审核状态
send:bid,state(-1fail,1pass)
resp:1-succ,-1-login,-2-fail
'''
def verifyState(request):  
    pass

'''
修改书籍信息
send:bid,info(…………)
resp:1-succ,-1-login,-2-fail
'''
def verifyAlterBook(request):  
    pass

'''
删除书籍
send:bid
resp:1-succ,-1-login,-2-fail
'''
def verifyDeleteBook(request):  
    pass





