#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''视图'''

from django.shortcuts import render
from SylDoc.utils.Tools import htmlResponse

from SylDoc.action.WebManagerAct import *

def homePage(request):
    return htmlResponse(request , '/SylDoc/HomePage/main/index.html') 

def manager(request):
    return htmlResponse(request , '/SylDoc/HomePage/manager/webLogin.html') 

