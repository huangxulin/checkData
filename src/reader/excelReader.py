# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: xulin.huang
'''
from reader.object import Reader as CustomReader
import xlrd

'''
excel导表格式如下：
备注1  备注2  备注3
字段名1  字段名2  字段名3
中文名1|格式  中文名2|格式  中文名3|格式
数据1  数据2  数据3
'''


class Reader(CustomReader):
    '''excel导表读取器
    '''
    
    def getFieldRowNo(self):
        return 2
    
    def getFormatRowNo(self):
        return 3
    
    def getDataBeginRowNo(self):
        return 4
    
    def readData(self):
        workBook = xlrd.open_workbook(self.getFullFileName())
        if workBook.nsheets < 1:
            return
        sheet = workBook.sheet_by_index(0)
        if sheet.nrows < 1 or sheet.ncols < 1:
            return
        for rowIndx in range(sheet.nrows):
            valueList = []
            for value in sheet.row_values(rowIndx):
                if isinstance(value, float):
                    if value == int(value) * 1.0:
                        value = int(value)
                value = str(value)
                valueList.append(value)
            
            line = "".join(valueList)
            if len(line) == 0:
                valueList = []
            self.transLineData(rowIndx + 1, valueList)
            
