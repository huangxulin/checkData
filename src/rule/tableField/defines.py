# -*- coding: utf-8 -*-
'''
Created on 2018年7月18日

@author: xulin.huang
'''

#===============================================================================
# 额外定义的导表字段规则配置
# 格式:
#    表名: {
#        "字段名1": "字段格式",
#        "字段名2": "字段格式",
#        "字段名3": "字段格式",
#    }
#
# 1.以"!"开头表示必填字段
# 2.RE表示正则表达式的字段格式，后面括号里的是正则表达式
#===============================================================================

tableFieldFormatList = {
    "tableField1_": {
        "id": "I", # 整数
        "elementId": "!I", # 必填且整数
        "weekday": "I",
        "sceneId": "I",
        "passReward": "I|L", # 整数或列表
        "missionIdStr": "RE(^\d+$)|IL", #整数或整数列表，效果与 "I|IL"一样
        "type": "I",
    },
     "tableField2_": {
        "id": "I",
        "elementId": "I",
        "weekday": "I",
        "sceneId": "I",
        "passReward": "I|L",
        "missionIdStr": "IL", # 整数列表
        "type": "I",
    },
}

