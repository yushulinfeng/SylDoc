#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户相关'''
from SylDoc.utils.check import checkUser, getPassWord
from SylDoc.utils.tools import webResponse
from SylDoc.models import User, WebManager

'''
用户注册
send:username,userpass
resp:1-succ,-1-name,-2-pass,-3-exist
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
        return webResponse(str(-1))
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 核对数据库
    db = User.objects.filter(username=username, userpass=userpass)
    state = -1
    for u in db:
        if u != None:
            state = 1
            break
    if state == 1:
        request.session['username'] = username
    return webResponse(str(state))

def managerLogin(request):  # 管理员登录
        # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    state = checkUser(username, userpass)
    if state:
        return webResponse(str(-1))
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 核对数据库
    db = WebManager.objects.filter(username=username, userpass=userpass)
    usertype = 0
    state = -1
    for u in db:
        if u != None:
            state = 1
            usertype = u.usertype
            break
    if state == 1:
        request.session['usertype'] = usertype
    return webResponse(str(state))

def managerAdd(request):  # 添加管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse(str(-1))
        # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    newtype = request.POST.get('usertype', '')
    state = checkUser(username, userpass)
    if state:
        return webResponse(str(state))
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 存入数据库
    db = WebManager(username=username, userpass=userpass, usertype=newtype)
    try:
        db.save()  # 这句是可能出现异常的，void方法，只能try-catch
        state = 1
    except:  # 已注册用户由于违反unique而抛出异常
        state = -3
    return webResponse(str(state))

def managerDel(request):  # 删除管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse(str(-1))
    pass

def managerAlter(request):  # 修改管理员类型
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse(str(-1))
    pass

def managerAll(request):  # 获取所有管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse(str(-1))
    pass



