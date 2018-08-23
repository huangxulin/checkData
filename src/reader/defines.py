# -*- coding: utf-8 -*-
'''
Created on 2018年7月9日

@author: xulin.huang
'''
import re

#===============================================================================
# 导表读取器配置
#===============================================================================
import reader.excelReader
import reader.textReader

readerModList = (
    ("\.xls$|\.xlsx$", reader.excelReader),
    ("\.txt$", reader.textReader),
)


# 测试
if __name__ == "__main__":
    fileNameList = {
        "sssd.xls",
        "guild.xlsx",
        "abce.txt",
    }

    for fileName in fileNameList:
        for pattern, readerMod in readerModList:
            m = re.search(pattern, fileName, re.I)
            if m:
                print("{:<15} match {}".format(fileName, pattern))