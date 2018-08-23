# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''
from rule.field.object import FieldRule as CustomFieldRule
from utils.typeCheck import *

class FieldRule(CustomFieldRule):
    '''检查整数
    '''
    
    def checkField(self, fieldObj):
        return isInteger(fieldObj.value)
        