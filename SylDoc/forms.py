#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''表单，对应model生成表单'''
# 目前现在此处直接写，后期建议仅在此处配置即可

from django.forms import ModelForm  
from SylDoc.models import Book  

######暂时先不用这个，以后再说
class BookAlterForm(ModelForm):  
    class Meta:  
        model = Book  
        # fields = '__all__' 
        fields = ['bid','name','cls','subcls','style','dynasty','describe',\
                  'word_title','word_describe','auth_name','auth_describe']   
