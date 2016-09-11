#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户相关'''
from SylDoc.utils.check import checkUser, getPassWord
from SylDoc.utils.tools import webResponse
from SylDoc.models import User

'''
用户注册
send:username,userpass
resp:1-succ,-1-name,-2-pass,-3-exist/other error
'''
def userRegister(request):  # 用户注册
    # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    state = checkUser(username, userpass)
    if state:
        return webResponse(str(state))
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 存入数据库
    db = User(username=username, userpass=userpass)
    try:
        db.save()  # 这句是可能出现异常的，void方法，只能try-catch
        state = 1
    except:  # 已注册用户由于违反unique而抛出异常
        state = -3
    return webResponse(str(state))

'''
用户登录
send:username,userpass
resp:1-succ,-1-fail
'''
def userLogin(request):  # 用户登录
    # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    state = checkUser(username, userpass)
    if state:
        return webResponse("-1")
    state = -1
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 核对数据库
    db = User.objects.filter(username=username, userpass=userpass)
    if db.exists():  # 数据存在，即登录成功
        state = 1
        request.session['username'] = username
    return webResponse(str(state))


