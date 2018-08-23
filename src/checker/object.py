# -*- coding: utf-8 -*-
'''
Created on 2018年7月6日

@author: xulin.huang
'''

class Checker(object):
    '''导表检查器(基类)
    '''
    
    def __init__(self):
        self.errorList = {} # 错误信息列表, {检查类型1:[信息1,信息2,...], 检查类型2:[信息1,信息2,...],...}
    
    def checkData(self, readerObj):
        '''检查数据
        '''
        self.errorList = {}
        for rowNo, fieldList in readerObj.iterData():
            self.checkLine(rowNo, fieldList)

    def checkLine(self, rowNo, fieldList):
        '''检查行
        '''
        for colNo, fieldObj in fieldList.items():
            if not self.checkField(fieldObj):
                errorList = self.errorList.setdefault("字段检查", [])
                errorList.append(self.getFieldInfo(fieldObj))
    
    def getFieldInfo(self, fieldObj):
        '''获取字段信息
        '''
        return str(fieldObj)
                
    def checkField(self, fieldObj):
        '''检查字段
                                各项目可以根据需求自定义此方法，而不使用字段规则
        '''
        if not fieldObj.value: # 字段值为空，不是必填字段可跳过
            if fieldObj.required:
                return False
            return True
        fieldRuleList = self.getFieldRuleList(fieldObj)
        if not fieldRuleList: # 没有规则，跳过
            return True
        for fieldRuleObj in fieldRuleList:
            if fieldRuleObj.checkField(fieldObj):
                return True
        return False

    def getFieldRuleList(self, fieldObj):
        '''获取字段规则列表
        '''
        fieldRuleList = []
        for fieldFormat in fieldObj.formatList:
            fieldRuleObj = rule.field.getFieldRule(fieldFormat)
            if fieldRuleObj:
                fieldRuleList.append(fieldRuleObj)
            
        return fieldRuleList
    
    def formatErrorInfo(self):
        '''格式化错误信息
        '''
        if not self.errorList:
            return ""

        infoList = []
        for checkType, errorList in self.errorList.items():
            info = "\n\t".join(errorList)
            infoList.append("{}:\n\t{}".format(checkType, info))
        return "\n".join(infoList)
        
        

import rule.field
import log
    
    