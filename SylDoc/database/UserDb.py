#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''用户类'''

from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)  # int
    username = models.CharField(max_length=255, unique=True)
    userpass = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.username
    
class WebManager(models.Model):
    username = models.CharField(max_length=255)
    userpass = models.CharField(max_length=255)
    usertype = models.IntegerField()
    
    def __unicode__(self):
        return self.username
    
