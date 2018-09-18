# -*- coding: utf-8 -*-
'''
Created on 2018年9月14日

@author: xulin.huang
'''
from checker.object import Checker as CustomChecker
from utils.typeCheck import *
import re
import table

class Checker(CustomChecker):
    
    def checkLine(self, rowNo, fieldList):
        '''检查行
        '''
        super().checkLine(rowNo, fieldList)
        
        # npcAppearance 导表
        self.npcAppearanceTable = table.getByLikeName("npcAppearance")
         
        for colNo, fieldObj in fieldList.items():
            fieldName = fieldObj.name
            value = fieldObj.value
            if not value:
                continue
            if fieldName == "npcAppearanceIdStr" and self.npcAppearanceTable:
                if not self.checkNpcAppearanceIdStr(value):
                    errorList = self.errorList.setdefault("npc外观检查", [])
                    errorList.append(self.getFieldInfo(fieldObj))
        
    def checkNpcAppearanceIdStr(self, value):
        '''npc外观检查
        '''
        readerObj = self.npcAppearanceTable
        appearanceIdList = value.split(",")
        for appearanceId in appearanceIdList:
            if not readerObj.findSameValueField(1, appearanceId):
                return False
        return True
            
