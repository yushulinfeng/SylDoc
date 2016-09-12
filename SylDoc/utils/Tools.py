#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from django.http import HttpResponse

# 允许js跨域的返回
def webResponse(resp_str):
    resp = HttpResponse(resp_str)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp

#获取当前日期，yyyy-mm-dd
def getTodayDate():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))
