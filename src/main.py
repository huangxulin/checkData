# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: xulin.huang
'''
import os
from config import *
import table
import sys

def start():
    '''开始检查导表
    '''
    for dataPath in dataPathList:
        for dirPath, dirNames, fileNames in os.walk(dataPath):
            for fileName in fileNames:
                if table.isIgnoreFile(fileName):
                    continue
                table.doRead(dirPath, fileName)
                
    table.checkAll()                
    table.checkDuplicateId()
            

if __name__ == "__main__":
    start()
    if table.isErorr(): # 检查有错误，通知调用者
        sys.exit(-1)