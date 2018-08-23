# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''

#===============================================================================
# 字段规则配置
#===============================================================================
import rule.field.fieldRuleI
import rule.field.fieldRuleF
import rule.field.fieldRuleN
import rule.field.fieldRuleS
import rule.field.fieldRuleL
import rule.field.fieldRuleIL
import rule.field.fieldRuleRE

ruleList = {
    "I": rule.field.fieldRuleI.FieldRule(), # 整数检查
    "F": rule.field.fieldRuleF.FieldRule(), # 小数检查
    "N": rule.field.fieldRuleN.FieldRule(), # 数字检查，如: "123"、"-123"、"123.4" 或 "-123.4"
    "S": rule.field.fieldRuleS.FieldRule(), # 字段串检查
    "L": rule.field.fieldRuleL.FieldRule(), # 列表(数组)检查，如: "1001,1002,1003"、"hp,mp,dam"
    "IL": rule.field.fieldRuleIL.FieldRule(), # 整数列表(数组)检查，如: "1001,1002,1003"、"1,2,3"
    "RE": rule.field.fieldRuleRE.FieldRule(), # 正则表达式检查，如: "^\d{3}"、"^[\d\w]+$"
    
}