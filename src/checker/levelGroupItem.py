# -*- coding: utf-8 -*-
'''
Created on 2018年8月10日

@author: xulin.huang
'''
from checker.object import Checker as CustomChecker
import re

class Checker(CustomChecker):
    
    def checkLine(self, rowNo, fieldList):
        '''检查行
        '''
        groupCount = 1 # 分组数
        for colNo, fieldObj in fieldList.items():
            if fieldObj.name == "groupRateStr":
                groupCount = fieldObj.value.count("_") + 1
                break

        errorFieldList = []
        for colNo, fieldObj in fieldList.items():
            fieldName = fieldObj.name
            if fieldName in ("itemsStr", "qualityStr"):
                count = fieldObj.value.count("_") + 1
                if count != groupCount:
                    errorFieldList.append(fieldName)
                    
        if errorFieldList:
            errorList = self.errorList.setdefault("分组数检查", [])
            errorList.append("行号:{},分组数要求:{},错误字段:({})".format(rowNo, groupCount, ",".join(errorFieldList)))
                
