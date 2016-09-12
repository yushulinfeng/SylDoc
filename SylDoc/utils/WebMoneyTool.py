#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''金币'''

from SylDoc.models import WebMoney

# 获取与修改金币数据

def moneyRegister(value=None):
    return moneyDeal(1)
    
def moneyLogin(value=None):####暂时备用，不添加了，不必写成独立方法
    return moneyDeal(2)

def moneyUpload(value=None):
    return moneyDeal(3)

def moneySearch(value=None):
    return moneyDeal(4)

# 获取所有金币列表
def moneyList():
    return WebMoney.objects.all()  # 后续的自己处理去吧

# 内部处理方法
# filter返回匹配列表，没有返回空表
# get返回单一匹配，没有或者有多于1条会报错
def moneyDeal(money_type, value=None):
    try:
        if(value == None):
            return WebMoney.objects.get(type=money_type).count  # 返回需要的数值
        else:
            return WebMoney.objects.filter(type=money_type).update(count=value)  # 返回影响的行数
    except:
        return 0

# 备用方法，以后再完善
def moneyRead():
    return moneyDeal(5)
def moneyDownload():
    return moneyDeal(6)



