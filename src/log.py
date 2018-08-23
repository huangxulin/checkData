# -*- coding: utf-8 -*-
'''日志
'''
'''
Created on 2018年7月5日

@author: xulin.huang
'''

def log(content, *args):
    if args:
        content = content.format(*args)
    gLog.write(content)
    print(content)
        
        
if "gLog" not in globals():
    global gLog
    gLog = open("debug.txt", "w")
