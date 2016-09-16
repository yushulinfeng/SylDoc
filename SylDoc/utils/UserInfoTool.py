#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户信息处理工具，后期会包含经验、金币增长算法'''

from SylDoc.models import  UserInfo

'''
更新用户信息(用于系统调用，增加用户经验金币等)（均为增加值,int）
resp:1-succ,-1-login,-2-fail
'''
def userInfoUpdate(userid, exp, rank, gold):
    db = UserInfo.objects.filter(userid=userid)
    for u in db:
        u.exp = u.exp + exp;
        u.rank = u.rank + rank;
        u.gold = u.gold + gold;
        u.save()
        return -1
    return 1
