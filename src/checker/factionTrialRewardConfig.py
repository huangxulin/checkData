# -*- coding: utf-8 -*-
'''
Created on 2018年9月13日

@author: xulin.huang
'''
from checker.object import Checker as CustomChecker
from utils.typeCheck import *
import re

class Checker(CustomChecker):
    
    def checkField(self, fieldObj):
        fieldName = fieldObj.name
        value = fieldObj.value
        if value:
            if fieldName == "itemWeightStr":
                return self.checkItemWeightStr(value)
            if fieldName == "itemStr":
                return self.checkItemStr(value)
        return True
    
    def checkItemWeightStr(self, value):
        if not isKV(value):
            return False
        for kv in value.split(","):
            if not re.match("^\d+:\d+$", kv):
                return False
        return True
    
    def checkItemStr(self, value):
        for s in value.split(","):
            if not re.match("^\d+:\d+:\d+$", s):
                return False
        return True
