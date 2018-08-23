# -*- coding: utf-8 -*-
'''
Created on 2018年7月18日

@author: xulin.huang
'''
from checker.object import Checker as CustomChecker

class Checker(CustomChecker):
    '''额外定义的导表字段检查器
                  这里使用额外定义的导表字段规则，需要在"rule.tableField.defines"配置
    '''
    def checkData(self, readerObj):
        self.errorList = {}
        fieldFormatList = rule.tableField.getFieldFormatList(readerObj.fileName)
        if not fieldFormatList: # 没有额外定义，跳过
            return
    
        # 根据额外配置设置字段格式
        for rowNo, fieldList in readerObj.iterData():
            for colNo, fieldObj in fieldList.items():
                fieldFormat = fieldFormatList.get(fieldObj.name)
                if fieldFormat:
                    fieldObj.setFieldFormat(fieldFormat)
        
        CustomChecker.checkData(self, readerObj)
    
import rule.tableField
