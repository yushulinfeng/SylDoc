#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

# 允许js跨域的返回
def webResponse(resp_str):
    resp = HttpResponse(resp_str)
    resp["Access-Control-Allow-Origin"] = "*"  # 允许跨域
    return resp
