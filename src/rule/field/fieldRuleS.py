# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''
from rule.field.object import FieldRule as CustomFieldRule

class FieldRule(CustomFieldRule):
    '''检查字符串
    '''
    
    def checkField(self, fieldObj):
        return isinstance(fieldObj.value, str)
        