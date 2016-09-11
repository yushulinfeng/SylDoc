#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''视图'''

from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.

def homePage(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/SylDoc/HomePage/index.html'))

