# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''

class FieldRule(object):
    '''字段检查规则
    '''
    
    def init(self, argStr):
        '''初始化参数
        '''
        pass
    
    def checkField(self, fieldObj):
        '''字段检查
                                    返回:布尔值
        '''
        raise Exception("请在子类实现方法 checkField")