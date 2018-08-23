# -*- coding: utf-8 -*-
'''
导表读取器相关
'''
import re

def getReader(dirPath, fileName):
    '''获取导表读取器
    '''
    import reader.defines
    for pattern, readerMod in reader.defines.readerModList:
        m = re.search(pattern, fileName, re.I)
        if m:
            return readerMod.Reader(dirPath, fileName)
    return None

