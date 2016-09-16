#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''管理员相关'''
# ok
from SylDoc.utils.UserCheckTool import checkUser, getPassWord, checkNick
from SylDoc.utils.Tools import webResponse
from SylDoc.models import  WebManager

'''
管理员登录
send:username,userpass
resp:1-succ,-1-fail
'''
def managerLogin(request):  # 管理员登录
    # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    state = checkUser(username, userpass)
    if state:
        return webResponse("-1")
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

'''添加管理员
send:username,userpass,usertype
resp:1-succ,-1-login,-2-power,-3-format,-4-error
'''
def managerAdd(request):  # 添加管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    if(usertype != '0' & usertype != '1'):  # 权限不够
        return webResponse("-2")
    # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    nickname = request.POST.get('nickname', '')
    newtype = request.POST.get('usertype', '')
    if checkUser(username, userpass):
        return webResponse("-3")
    if(nickname == None | nickname == ''):
        nickname = ''
    elif checkNick(nickname):
        return webResponse("-3")
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 存入数据库
    db = WebManager(username=username, userpass=userpass, usertype=newtype)
    try:
        db.save()  # 这句是可能出现异常的，void方法，只能try-catch
        return webResponse("1")
    except:  # 已注册用户由于违反unique而抛出异常
        return webResponse("-4")

'''
删除管理员
send:username
resp:1-succ,-1-login,-2-power,-3error
'''
def managerDel(request):  # 删除管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse(str(-1))
    if(usertype != '0' & usertype != '1'):  # 权限不够
        return webResponse(str(-2))
    username = request.POST.get('username', '')
    # 查找数据库
    db = WebManager.objects.filter(username=username)
    for u in db:
        if u != None:
            u.delete()
            return webResponse("1")
    return webResponse("-3")

'''
修改管理员类型
send:username,usertype
resp:1-succ,-1-login,-2-power,-3error
'''
def managerAlter(request):  # 修改管理员类型
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    if(usertype != '0' & usertype != '1'):  # 权限不够
        return webResponse("-2")
    username = request.POST.get('username', '')
    newtype = request.POST.get('usertype', '')
    # 更新数据库（先获取，在保存也可）
    db = WebManager.objects.filter(username=username)
    try:
        db.update(usertype=newtype)
        return webResponse("1")
    except:   
        return webResponse("-3")

'''
获取所有管理员
send:username,usertype
resp:json-succ,-1-login
'''
def managerAll(request):  # 获取所有管理员
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    # 核对数据库
    db = WebManager.objects.all()
    res = "["
    for u in db:
        if u != None:
            if res != "[" :
                res += ","
            res += "{'name':'" + u.username + "','type':" + u.usertype + "}";
    res += "]"
    return webResponse(res)



