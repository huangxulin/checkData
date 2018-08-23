# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: xulin.huang
'''
from reader.object import Reader as CustomReader

'''
文本导表格式如下：
字段名1|格式  字段名2|格式  字段名3|格式
数据1  数据2  数据3
'''

class Reader(CustomReader):
    '''文本导表读取器
    '''
    
    def getFieldRowNo(self):
        return 1
    
    def getFormatRowNo(self):
        return 1
    
    def getDataBeginRowNo(self):
        return 2
    
    def readData(self):
        rowNo = 0
        with open(self.getFullFileName(), "r") as fileObj:
            for line in fileObj:
                line = line.strip()
                rowNo += 1
                if len(line) == 0:
                    valueList = []
                else:
                    valueList = line.split("\t")
                self.transLineData(rowNo, valueList)
