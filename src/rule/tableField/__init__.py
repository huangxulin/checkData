# -*- coding: utf-8 -*-
'''额外定义的导表字段规则
'''
import re

def getFieldFormatList(fileName):
    '''获取额外定义字段格式列表
    '''
    import rule.tableField.defines
    for pattern, fieldFormatList in rule.tableField.defines.tableFieldFormatList.items():
        if re.match(pattern, fileName):
            return fieldFormatList
    return {}