# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: xulin.huang
'''

#===============================================================================
# 以下为默认配置
# 策划需要根据自己实际的导表目录修改这里
#===============================================================================

# 导表目录
dataPathList = (
    "d:\D导表",
)


# 忽略文件列表(这里的导表文件不检查)
ignoreFileList = (
    "^~", # excel临时文件
    ".*\.csv", # 自动生成的导表
    ".*\.bak", # UltraEdit备份文件
    "chatWord", # 敏感字库
)

# 关联导表，会检查重复id
joinFileList = (
    ("npcGeneral", "npcDynamicMonster",),
    ("npcGeneral", "npcDynamicMonster",),
)