#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

# 获取PDF对应的路径--网址
def getBookPdfNetPath(bid):
    return "/SylDoc/HomePage/_server_/book/pdf/" + bid + ".pdf";

# 获取Word对应的路径(仅支持doc,暂不处理docx)--网址
def getBookWordNetPath(bid):
    return "/SylDoc/HomePage/_server_/book/word/" + bid + ".doc";

# 获取PDF对应的路径-服务器
def getBookPdfLocalPath(bid):
    initBookLocalDir()
    return  os.getcwd() + "/SylDoc/static/_server_/book/pdf/" + bid + ".pdf";

# 获取Word对应的路径(仅支持doc,暂不处理docx)-服务器
def getBookWordLocalPath(bid):
    initBookLocalDir()
    return  os.getcwd() + "/SylDoc/static/_server_/book/word/" + bid + ".doc";

# 初始化处存储文件夹
def initBookLocalDir():
    path = os.getcwd() + "/SylDoc/static/_server_/book/pdf/";
    if os.path.exists(path):
        os.makedirs(path)
    path = os.getcwd() + "/SylDoc/static/_server_/book/word/";
    if os.path.exists(path):
        os.makedirs(path)

# 获取书籍随机ID值，用于生成ID   
def getBookRandomId(userid):
    return time.strftime('%Y%m%d_%H%M%S_', time.localtime(time.time())) + userid

# 获取书籍上传时间 
def getBookCurrentTime():
    return time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))
            
            
            
            
            
            
            
