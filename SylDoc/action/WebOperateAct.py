#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''事件管理相关，内容与运营'''
# ok
# 管理员体系，目前权限区分体现在页面，暂不在后台进行约束。后期可修改。
# 原计划1super-3normal,页面上暂时整合为2个

from SylDoc.utils.Tools import webResponse
from SylDoc.utils.WebIndexTool import pushList, pushAlter
from SylDoc.utils.WebMoneyTool import moneyList, moneyDeal

'''
金币奖励修改
send:type,count
resp:1-succ,-1-login,-2-fail
'''
def operateMoneyAlter(request):
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    money_type = request.POST.get('type', '')
    count = request.POST.get('count', '')
    if moneyDeal(money_type, count) != 0:
        return webResponse("1")
    return webResponse("-2")

'''
添加首页数据
send:bid,note,type(目前只有1，不用传了，暂不处理)
resp:1-succ,-1-login,-2-fail
'''
def operateIndexAdd(request):
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    bid = request.POST.get('bid', '')
    note = request.POST.get('note', '')
    # money_type = request.POST.get('type', '')
    if pushAlter(bid, note) != 0:
        return webResponse("1")
    return webResponse("-2")

'''
删除首页数据
send:id
resp:1-succ,-1-login,-2-fail
'''
def operateIndexDel(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    bid = request.POST.get('bid', '')
    if pushAlter(bid, None, True) != 0:
        return webResponse("1")
    return webResponse("-2")

'''
获取金币奖励列表
send:null
resp:json-succ,-1-login
'''
def operateMoneyList(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    db = moneyList()
    res = "["
    for m in db:
        if res != "[" :
            res += ","
        res += "{'type':" + m.type + ",'note':'" \
        + m.note + "','count':" + m.count + "}"
    res += "]"
    return webResponse(res)

'''
获取首页数据列表(暂不考虑分页)
send:null
resp:json-succ,-1-login,-2-fail
'''
def operateIndexList(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    db = pushList()
    res = "["
    for m in db:
        if res != "[" :
            res += ","
        res += "{'bid':" + m.bid + ",'note':'" \
        + m.note + "','type':" + m.type + "}"
    res += "]"
    return webResponse(res)
    
    
    
    
    
    

