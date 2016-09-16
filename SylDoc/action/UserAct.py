#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户相关'''
# ok
from SylDoc.utils.UserCheckTool import checkUser, checkNick, getPassWord
from SylDoc.utils.Tools import webResponse, getTodayDate
from SylDoc.utils.WebMoneyTool import moneyRegister
from SylDoc.models import User, UserInfo

'''
用户注册
send:username,userpass
resp:1-succ,-1-name,-2-pass,-3-昵称，-4-exist/other error
'''
def userRegister(request):  # 用户注册
    # 获取参数
    username = request.POST.get('username', '')
    userpass = request.POST.get('userpass', '')
    nickname = request.POST.get('nickname', '') 
    state = checkUser(username, userpass)
    if state:
        return webResponse(str(state))
    if checkNick(nickname):  # 必须填写合法昵称
        return webResponse("-3")
    # 用户密码加密
    userpass = getPassWord(userpass)
    # 存入数据库
    db = User(username=username, userpass=userpass)
    try:
        db.save()  # 这句是可能出现异常的，void方法，只能try-catch
    except:  # 已注册用户由于违反unique而抛出异常
        return webResponse("-4")
    # 需要获取最新的注册初始金币
    # 因为不进行save是没有userid的
    db_info = UserInfo(userid=db.userid, nickname=nickname, \
                        exp=0, rank=0, gold=moneyRegister(), getTodayDate())
    try:
        db_info.save()  
    except:
        return webResponse("-4")
    return webResponse("1")

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
        # ##可以考虑根据登录日期判断首次登录，给予奖励
    return webResponse(str(state))


'''
用户修改密码
send:oldpass,newpass/session
resp:1-succ,-1-fail
'''
def userAlterPass(request):
    pass



# 用户忘记密码（暂不处理）



