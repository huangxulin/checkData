# -*- coding: utf-8 -*-
'''
信息打印相关
'''
'''
Created on 2018年7月7日

@author: xulin.huang
'''
import re

def printClassInfo(object):
    info = str(object.__class__)
    m = re.match("<class '(.+)'>", info)
    if m:
        return m.group(1)
    return info