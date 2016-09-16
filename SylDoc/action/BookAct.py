#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''书籍相关'''
# ok-need test
from SylDoc.utils.Tools import webResponse
from SylDoc.utils.BookTool import getBookRandomId, getBookCurrentTime
from SylDoc.utils.BookTool import getBookPdfLocalPath, getBookWordLocalPath
from SylDoc.utils.BookTool import getBookPdfNetPath, getBookWordNetPath 
from SylDoc.models import Book, BookState
from django.db.models.query_utils import Q
from SylDoc.forms import BookAlterForm

'''
书籍普通搜索
send:condition
resp:json-succ,-2-fail
'''
def bookSearchNormal(request):  # 书名，作者名
    name = request.POST.get('condition', '')
    db = Book.objects.filter((Q(name__icontains=name) | Q(author__icontains=name))\
                             & Q(check_state=1))
    res = "["
    for b in db:  # 暂时先返回这些信息
        if res != "[" :
            res += ","
        res += "{'bid':" + b.bid + ",'name':'" \
        + b.name + "','describe':'" + b.describe + "'}"
    res += "]"
    return webResponse(res)


'''
书籍高级搜索
send:condition(name……)
resp:json-succ,-2-fail
'''
def bookSearchAdvance(request):
    name = request.POST.get('name', '')
    author = request.POST.get('author', '')
    dynasty = request.POST.get('dynasty', '')
    cls = request.POST.get('cls', '')
    subcls = request.POST.get('subcls', '')
    style = request.POST.get('style', '')
    sql = Q(check_state=1)
    if(name != ''):
        sql &= Q(name__icontains=name)
    if(author != ''):
        sql &= Q(author__icontains=author)
    if(dynasty != ''):
        sql &= Q(dynasty__icontains=dynasty)
    if(cls != ''):
        sql &= Q(cls__exact=cls)
    if(subcls != ''):
        sql &= Q(subcls__exact=subcls)
    if(style != ''):
        sql &= Q(style__exact=style)
    db = Book.objects.filter(sql)
    res = "["
    for b in db:  # 暂时先返回这些信息
        if res != "[" :
            res += ","
        res += "{'bid':" + b.bid + ",'name':'" \
        + b.name + "','describe':'" + b.describe + "'}"
    res += "]"
    return webResponse(res)

'''
书籍阅读
send:bid
resp:json-succ,-2-fail
'''
#####需要测试
def bookRead(request): 
    # ##此处暂时没有想到更好的办法，就先返回pdf/word文件路径吧
    # ##后期要考虑安全问题，不能将重要文件放在static下，此时为方便先这样处理
    # 处理方式：根据bid推算书籍的存储路径，并返回其他信息
    bid = request.POST.get('bid', '')
    db = Book.objects.filter(bid=int(bid)) 
    res = ""
    for b in db:
        res += "{'book':" + b.toJson() + "','pdf':'" + getBookPdfNetPath(bid) \
        + "','word':'" + getBookWordNetPath(bid) + "'}";
        return webResponse(res)
    return webResponse("-2")

'''
书籍上传
send:book(……)
resp:1-succ,-1-login,-2-fail，-3-filefail
'''
def bookUpload(request):
    # 登录状态判断
    userid = request.session['userid']
    if(userid == None):  # 未登录
        return webResponse("-1")
    # 表单获取
    form = BookAlterForm(request.POST)  # 自动封装表单对象(###一定要测试)
    if not form.is_valid():
        return webResponse("-2")
    # commit暂时获取一个数据库对象，对其他字段进行赋值
    bid = getBookRandomId(userid);
    try:
        temp = form.save(commit=False) 
        temp.bid = bid
        temp.check_state = 0
        temp.save()  # 真正插入数据库
        # 存储到状态数据库
        db = BookState(bid=bid, uploader=userid, upload_time=getBookCurrentTime())
        db.save()
    except:
        return webResponse("-2")
    # 获取文件
    pdf = request.FILES.get('pdf', None)
    word = request.FILES.get('word', None)
    if pdf == None | word == None:
        return webResponse("-3")
    try:
        stream = open(getBookPdfLocalPath(bid), 'wb+')
        for chunk in pdf.chunks():
            stream.write(chunk)
        stream.close()
        stream = open(getBookWordLocalPath(bid), 'wb+') 
        for chunk in word.chunks():
            stream.write(chunk)
        stream.close()
    except:
        return webResponse("-3")
    return webResponse("1")


####将来的核心功能之一，暂不处理
'''
书籍内容搜索（####这个是核心内容，但实现略麻烦，暂时放置一下）
send:conditio(……)
resp:json-succ,-1-login,-2-fail
'''
def bookSearchContent(request): 
    pass





