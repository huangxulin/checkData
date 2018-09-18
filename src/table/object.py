# -*- coding: utf-8 -*-
'''
Created on 2018年9月14日

@author: xulin.huang
'''

class TableManager(object):
    '''导表管理器
    '''
    
    def __init__(self):
        self.tableList = {} # 导表列表
        
    def add(self, fileName, readerObj):
        '''增加导表
        '''
        self.tableList[fileName] = readerObj
        
    def getByLikeName(self, likeName):
        '''根据文件名获取类似的导表
        '''
        for fileName, readerObj in self.tableList.items():
            if likeName in fileName:
                return readerObj
        return None
        