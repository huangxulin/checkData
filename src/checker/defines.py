# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''
import re

#===============================================================================
# 导表检查器配置
#===============================================================================
import checker.generalChecker
import checker.tableFiledChecker
import checker.fallItem
import checker.levelGroupItem
import checker.factionTrialRewardConfig
import checker.npcDynamicMonster

checkerList = (
    (".*", checker.generalChecker.Checker()), # 通用检查器
    (".*", checker.tableFiledChecker.Checker()), # 额外定义的导表字段检查器
    ("fallItem_", checker.fallItem.Checker()), # fallItem表检查器
    ("levelGroupItem_", checker.levelGroupItem.Checker()), # levelGroupItem表检查器
    ("factionTrialRewardConfig_", checker.factionTrialRewardConfig.Checker()), # factionTrialRewardConfig表检查器
    ("npcDynamicMonster_", checker.npcDynamicMonster.Checker()), # npcDynamicMonster表检查器
)



if __name__ == "__main__":
    fileNameList = {
        "sssd.xls.txt",
        "要.xlsx",
        "abce.txt",
    }
  
    for fileName in fileNameList:
        for pattern, checker in checkerList:
            m = re.search(pattern, fileName, re.I)
            if m:
                print("{:<15} match {}".format(fileName, pattern))