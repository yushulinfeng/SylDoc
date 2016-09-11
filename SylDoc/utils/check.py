#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''格式检查'''

import re
import hashlib
from django.contrib.auth.mixins import UserPassesTestMixin

# 用户相关的检查
def checkUser(username, userpass, nickname=None):
    # 邮箱验证
    pattern = re.compile(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$')
    match = pattern.match(username)
    if not match:
        return -1;
    # 密码验证
    pattern = re.compile(r'^\w{4,20}$')
    match = pattern.match(userpass)
    if not match:
        return -2;
    return 0;
    
def checkNick(nickname):
        # 昵称验证
        pattern = re.compile(u'^[a-zA-Z0-9\u4E00-\u9FA5_]{1,20}$')
        match = pattern.match(nickname)
        if not match:
            return -1;
        return 0;
    
# 用户密码加密
def getPassWord(userpass):
    # 两次MD5
    md5 = hashlib.md5()
    md5.update(userpass)
    userpass = md5.hexdigest()
    md5.update(userpass)
    userpass = md5.hexdigest()
    return userpass;
