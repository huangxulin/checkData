# -*- coding: utf-8 -*-
'''
Created on 2018年7月7日

@author: xulin.huang
'''

def test():
    import re
    fieldFormat = "I2_\d{1:3}$"
    argStr = ""
    m = re.match("^(\w+)_(.*)$", fieldFormat)
    if m:
        fieldFormat = m.group(1)
        argStr = m.group(2)
    
    print(fieldFormat)
    print(argStr)
        
if __name__ == "__main__":
    test()