# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: xulin.huang
'''
import os

class Reader(object):
    '''导表读取器(基类)
    '''
    
    def __init__(self, dirPath, fileName):
        self.dirPath = dirPath # 导表文件所在目录
        self.fileName = fileName # 导表文件名
        self.fullFileName = os.path.join(dirPath, fileName) # 导表文件全路径
        self.data = {} # 导表数据，如: {1:{1:field1,2:field2,...}, 2:{1:field1,2:field2,...},}
        self.fieldNameList = {} # 字段名列表，如: {1:fieldName1,2:fieldName2,...}
        self.formatList = {} # 格式列表，如: {1:format1,2:format2,...}
        self.blankRowNoList = [] # 空行的行号列表，如: [行号1,行号5,行号7,...]
        
    def getFileName(self):
        return self.fileName
        
    def getFullFileName(self):
        return self.fullFileName
    
    def getFieldRowNo(self):
        '''字段名行号
                            该行内容如: id、name
        '''
        raise Exception("请在子类实现方法 getFieldRowNo")
    
    def getFieldNameByColNo(self, colNo):
        '''根据列号获取字段名
        '''
        return self.fieldNameList.get(colNo, None)
    
    def transFieldName(self, fieldName):
        '''转换成字段名
                            假如字段名附加了信息，就需要在这里过滤掉，如: id|I、text|S
        '''
        strList = fieldName.split("|", 1)
        if len(strList) == 2:
            return strList[0]
        return fieldName
    
    def transToFieldNameList(self, valueList):
        '''转换成字段名列表
        '''
        self.fieldNameList = {}
        for colIndex, value in enumerate(valueList):
            colNo = colIndex + 1
            self.fieldNameList[colNo] = self.transFieldName(value)
    
    def getFormatRowNo(self):
        '''数据格式行号
                            该行内容如: 编号|I、名称|S
        '''
        raise Exception("请在子类实现方法 getFormatRowNo")
    
    def getFormatByColNo(self, colNo):
        '''根据列号获取格式
        '''
        return self.formatList.get(colNo, "")
    
    def transFormat(self, fieldFormat):
        '''获取字段格式
                            一般情况 下，格式是附加在字段后面的，所以需要过滤出来，如: 编号|I、名称|S
        可以支持多个字段格式，如: 奖励|I|L
        '''
        strList = fieldFormat.split("|", 1)
        if len(strList) == 2:
            return strList[1]
        return ""
    
    def transToFormatList(self, valueList):
        '''转换成格式列表
        '''
        self.formatList = {}
        for colIndex, value in enumerate(valueList):
            colNo = colIndex + 1
            self.formatList[colNo] = self.transFormat(value)
        
    def getDataBeginRowNo(self):
        '''导表数据开始行号
                            该行内容如: 编号|I、名称|S
        '''
        raise Exception("请在子类实现方法 getDataBeginRowNo")
    
    def iterData(self):
        '''迭代导表数据
                            迭代顺序：行号升序
        '''
        rowNoList = list(self.data.keys())
        rowNoList.sort()
        for rowNo in rowNoList:
            yield rowNo, self.data[rowNo]
            
    def iterColData(self, colNo):
        '''根据列号迭代导表数据
        '''
        if colNo > self.getColCount():
            return
        
        rowNoList = list(self.data.keys())
        rowNoList.sort()
        for rowNo in rowNoList:
            fieldObj = self.data[rowNo].get(colNo)
            if fieldObj:
                yield rowNo, fieldObj

    def readData(self):
        '''读取导表数据
        '''
        raise Exception("请在子类实现方法 readData")
    
    def transLineData(self, rowNo, valueList):
        '''转换行数据
        '''
        if rowNo < self.getDataBeginRowNo():
            if rowNo == self.getFieldRowNo(): # 字段名行
                self.transToFieldNameList(valueList)
            if rowNo == self.getFormatRowNo(): # 格式行
                self.transToFormatList(valueList)
            return
        
        if len(valueList) == 0: # 空的数据行
            self.blankRowNoList.append(rowNo)
            return
        
        # 下面是数据行的转换
        fieldObjList = {}
        for colIndex, value in enumerate(valueList):
            colNo = colIndex + 1
            fieldName = self.getFieldNameByColNo(colNo)
            if not fieldName:
                break
            fieldFormat = self.getFormatByColNo(colNo)
            fieldObjList[colNo] = self.newField(fieldName, value, fieldFormat, rowNo, colNo)
        self.data[rowNo] = fieldObjList
        
    def newField(self, fieldName, fieldValue, fieldFormat, rowNo, colNo):
        '''创建字段
        '''
        fieldObj = Field(fieldName, fieldValue, fieldFormat, rowNo, colNo)
        fieldObj.fileName = self.fileName
        return fieldObj
    
    def getRowCount(self):
        '''获取行数
        '''
        return len(self.data)
    
    def getColCount(self):
        '''获取列数
        '''
        return len(self.fieldNameList)
    
    def getBlankRowNoList(self):
        '''空行的行号列表
        '''
        return self.blankRowNoList
    
    def getDuplicateIdList(self):
        '''获取重复id列表
        '''
        idList = {}
        for rowNo, fieldObj in self.iterColData(1):
            idValue = fieldObj.value
            fieldList = idList.setdefault(idValue, [])
            fieldList.append(fieldObj)
            
        duplicateIdList = []
        for idValue, fieldList in idList.items():
            if len(fieldList) > 1:
                duplicateIdList.append(idValue)
        return duplicateIdList
    
    def findSameValueField(self, colNo, value):
        '''搜寻相同值的字段
        '''
        for rowNo, fieldObj in self.iterColData(colNo):
            if fieldObj.value == value:
                return fieldObj
        return None
            
    
    def __str__(self):
        infoList = []
        infoList.append("  文件名:{}".format(self.fileName))
        infoList.append("  行数:{}".format(self.getRowCount()))
        infoList.append("  列数:{}".format(self.getColCount()))
        infoList.append("  字段名列表:{}".format(",".join(self.fieldNameList.values())))
        infoList.append("  格式列表:{}".format(",".join(self.formatList.values())))
        return "{{\n{}\n}}".format("\n".join(infoList))
    

class Field(object):
    '''字段
    '''
    
    def __init__(self, name, value, fieldFormat, rowNo, colNo):
        self.name = name # 字段名
        self.value = value # 字段值
        self.required = False # 是否必填
        self.formatStr = fieldFormat # 格式字符串
        self.formatList = [] # 字段格式列表，格式可以有多个
        if fieldFormat:
            self.setFieldFormat(fieldFormat)
        self.rowNo = rowNo # 行号
        self.colNo = colNo # 列号
        self.fileName = "" # 导表文件名
        
    def setFieldFormat(self, fieldFormat):
        '''设置字段格式
        '''
        self.formatStr = fieldFormat
        if fieldFormat.startswith("!"):
            self.required = True
            fieldFormat = fieldFormat[1:]
        if fieldFormat:
            self.formatList = re.findall("\w+\(.+\)|\w+", fieldFormat)
        
    def __str__(self):
        infoList = []
        infoList.append("字段名:{}".format(self.name))
        infoList.append("行号:{}".format(self.rowNo))
        infoList.append("列号:{}".format(self.colNo))
        infoList.append("格式:{}".format(self.formatStr))
        infoList.append("字段值:'{}\'".format(self.value))
        return "{}".format(",".join(infoList))
        
    
import re
    