# -*- coding: utf-8 -*-
'''
字段检查规则相关
'''

def getFieldRule(fieldFormat):
    '''获取字段检查规则
    '''
    import rule.field.defines

    argStr = "" # 初始化参数
    m = re.match("^(\w+)\((.*)\)$", fieldFormat)
    if m:
        fieldFormat = m.group(1)
        argStr = m.group(2)
        
    fieldRuleObj = rule.field.defines.ruleList.get(fieldFormat, None)
    if fieldRuleObj:
        fieldRuleObj.init(argStr)
    return fieldRuleObj


import re
    
