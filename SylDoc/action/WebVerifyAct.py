#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''管理书籍相关，审核与修改'''
# ok-need test
from SylDoc.utils.Tools import webResponse
from SylDoc.models import  Book
from SylDoc.forms import BookAlterForm

'''
获取需要审核书籍里列表(暂不考虑分页)
send:null
resp:json-succ,-1-login
'''
def verifyList(request):  
    # ## 后期考虑，点击(bid)查看书籍详情
    # ##此处建议用table显示信息即可，后边加两个按钮agree/dis即可
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    db = Book.objects.filter(check_state=0)
    res = "["
    for b in db:
        if res != "[" :
            res += ","
        res += "{'bid':" + b.bid + ",'name':'" \
        + b.name + "','describe':'" + b.describe + "'}"
    res += "]"
    return webResponse(res)

'''
审核书籍，设定审核状态
send:bid,state(-1fail,1pass)
resp:1-succ,-1-login,-2-fail
'''
def verifyState(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    bid = request.POST.get('bid', '')
    state = request.POST.get('state', '')
    db = Book.objects.filter(bid=int(bid))  # 考虑是否需要类型转换
    for b in db:
        b.state = int(state)
        b.save()
        return webResponse("1")
    return webResponse("-2")

'''
修改书籍信息
send:bid,info(…………)
resp:1-succ,-1-login,-2-fail
'''
def verifyAlterBook(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    form = BookAlterForm(request.POST)  # 自动封装表单对象
    if form.is_valid():  
#         print form.bid    ####测试一下，这个我不太确定
#         print form.Meta.model.bid
        db = Book.objects.filter(bid=form.bid)  # 考虑是否需要类型转换
        for b in db:
            b.name = form.name
            b.cls = form.cls
            b.subcls = form.subcls
            b.style = form.style
            b.dynasty = form.dynasty
            b.describe = form.describe
            b.word_title = form.word_title
            b.word_describe = form.word_describe
            b.auth_name = form.auth_name
            b.auth_describe = form.auth_describe
            b.save()
            return webResponse("1")
    return webResponse("-2")
    pass

'''
删除书籍
send:bid
resp:1-succ,-1-login,-2-fail
'''
def verifyDeleteBook(request):  
    usertype = request.session['usertype']
    if(usertype == None):  # 未登录
        return webResponse("-1")
    bid = request.POST.get('bid', '')
    db = Book.objects.filter(bid=int(bid))  # 考虑是否需要类型转换
    for b in db:
        try:
            b.delete()
            return webResponse("1")
        except:
            return webResponse("-2")
    return webResponse("-2")




