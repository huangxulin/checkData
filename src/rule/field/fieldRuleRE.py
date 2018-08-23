# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''
from rule.field.object import FieldRule as CustomFieldRule
import re

class FieldRule(CustomFieldRule):
    '''检查整数列表(数组)
    '''

    def init(self, argStr):
        '''初始化参数
        '''
        self.pattern = argStr # 正则表达式
    
    def checkField(self, fieldObj):
        return re.match(self.pattern, fieldObj.value)
                
        