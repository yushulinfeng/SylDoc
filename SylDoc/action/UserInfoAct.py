#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户信息相关'''
# ok
from SylDoc.utils.UserCheckTool import  checkNick
from SylDoc.utils.Tools import webResponse
from SylDoc.models import  UserInfo

'''
获取用户信息（目前仅自己能看）
send:null/session
resp:json-succ,-1-login,-2-fail
'''
def userInfoGet(request): 
    userid = request.session['userid']
    if(userid == None):  # 未登录
        return webResponse("-1")
    db = UserInfo.objects.filter(userid=userid)
    for u in db:  # nickname,exp,rank,gold
        res = "{'nick':'" + u.nickname + "','exp':" + u.exp \
        + ",'rank':" + u.rank + ",'gold':" + u.gold + "}";
        return webResponse(res)
    return webResponse("-2")

'''
修改用户信息(目前只能修改：nickname)
send:info(nickname……)/session
resp:1-succ,-1-login,-2-fail
'''
def userInfoAlter(request):
    userid = request.session['userid']
    if(userid == None):  # 未登录
        return webResponse("-1")
    nickname = request.POST.get('nickname', '')
    if(nickname == "" | checkNick(nickname) != 0):
        return webResponse("-2")
    db = UserInfo.objects.filter(userid=userid)
    for u in db:   
        u.nickname = nickname
        u.save()
        return webResponse("1")
    return webResponse("-2")

'''
获取用户公开你信息（用于别人查看，暂不处理）
send:userid
resp:json-succ,-1-login,-2-fail
'''
def userInfoGetPublic(request): 
    pass

