#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''书籍相关'''

from SylDoc.utils.UserCheckTool import checkUser, checkNick, getPassWord
from SylDoc.utils.Tools import webResponse, getTodayDate
from SylDoc.models import Book, BookState

'''
书籍普通搜索
send:condition
resp:json-succ,-2-fail
'''
def bookSearchNormal(request): 
    pass


'''
书籍高级搜索
send:condition(……)
resp:json-succ,-2-fail
'''
def bookSearchAdvance(request): 
    pass

'''
书籍内容搜索
send:conditio(……)
resp:json-succ,-1-login,-2-fail
'''
def bookSearchContent(request): 
    pass

'''
书籍阅读
send:bid
resp:json-succ,-2-fail
'''
def bookRead(request): 
    pass

'''
书籍上传
send:book(……)
resp:json-succ,-1-login,-2-fail
'''
def bookUpload(request): 
    pass

