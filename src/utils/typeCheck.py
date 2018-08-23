# -*- coding: utf-8 -*-
'''
类型检查相关
'''
'''
Created on 2018年7月9日

@author: xulin.huang
'''
import re

def isInteger(s):
    '''是否整形
    '''
    if isinstance(s, int):
        return True
    if isinstance(s, str):
        m = re.match("^[+-]?\d+$", s)
        if m:
            return True
    return False

def isFloat(s):
    '''是否小数
    '''
    if isinstance(s, float):
        return True
    if isinstance(s, str):
        m = re.match("^[+-]?\d+\.\d+$", s)
        if m:
            return True
    return False

def isNumber(s):
    '''是否数字
    '''
    if isInteger(s):
        return True
    if isFloat(s):
        return True
    return False

def isList(s):
    '''是否列表
    '''
    if not isinstance(s, str):
        return False
    lst = s.split(",")
    return len(lst) >= 2
        


if __name__ == "__main__":
    print(isList("A"))
    
