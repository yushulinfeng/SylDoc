#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户信息相关'''

from SylDoc.utils.Tools import webResponse, getTodayDate
from SylDoc.utils.WebMoneyTool import moneyRegister
from SylDoc.models import User, UserInfo

'''
获取用户信息（目前仅自己能看）
send:null
resp:json-succ,-1-login,-2-fail
'''
def userInfoGet(request): 
    pass

'''
修改用户信息
send:info(…………)
resp:1-succ,-1-login,-2-fail
'''
def userInfoAlter(request):
    pass


'''
获取用户公开你信息（用于别人查看，暂不处理）
send:userid
resp:json-succ,-1-login,-2-fail
'''
def userInfoGetPublic(request): 
    pass

