# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: xulin.huang
'''
from checker.object import Checker as CustomChecker
import re

class Checker(CustomChecker):
    
    def checkField(self, fieldObj):
        if fieldObj.name == "items":
            itemList = fieldObj.value.split(",")
            for item in itemList:
                if not re.match("^\d+:\d+:\d+:\d+:\d+$", item):
                    return False
        return True
