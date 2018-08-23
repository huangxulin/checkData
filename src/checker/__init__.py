# -*- coding: utf-8 -*-
'''
导表检查器相关
注意：可以使用多个检查器来检查同一个导表
'''
import re

def getCheckerList(fileName):
    '''获取导表检查器列表
    '''
    import checker.defines

    lst = []
    for pattern, checkerObj in checker.defines.checkerList:
        m = re.search(pattern, fileName, re.I)
        if m:
            lst.append(checkerObj)
    return lst
 
 
