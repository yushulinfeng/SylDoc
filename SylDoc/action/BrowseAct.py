#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''浏览相关'''
# ok
from SylDoc.utils.Tools import webResponse
from SylDoc.utils.WebIndexTool import pushList

'''
获取首页推荐的信息
send:null
resp:json-succ
'''
def BrowseIndexRecommend(request): 
    # 此处为方便处理，返回bid与note，note用于底部显示。(09-17)
    # 后期需要联动书籍数据库，获取bid对应的封面或其他信息，或让管理员添加
    db = pushList()
    res = "["
    for m in db:
        if res != "[" :
            res += ","
        res += "{'bid':" + m.bid + ",'note':'" \
        + m.note + "}"
    res += "]"
    return webResponse(res)


'''
获取首页最新书籍的信息（暂不处理）
send:null
resp:json-succ,-2-fail
'''
def BrowseIndexNewBook(request): 
    pass
 
 
 
 
