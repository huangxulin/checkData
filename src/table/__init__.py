# -*- coding: utf-8 -*-
'''
导表处理
一个导表，读取器只有1个，检查器可以多个
'''

def handle(dirPath, fileName):
    readerObj = reader.getReader(dirPath, fileName)
    if not readerObj:
#         log.log("导表找不到读取器:{}", fileName)
        return
    checkerList = checker.getCheckerList(fileName)
    if not checkerList:
        setError(True)
        log.log("导表找不到任何检查器:{}", fileName)
        return
    
    try:
        readerObj.readData()
#         print(readerObj, "\n")
    except:
        setError(True)
        log.log("导表读取错误, reader:{},fileName:{}", printInfo.printClassInfo(readerObj), fileName)
        traceback.print_stack(log.log)
        return
    
    gTableList[fileName] = readerObj
    doCheck(fileName, readerObj, checkerList)
    
def doCheck(fileName, readerObj, checkerList):
    '''执行检查
    '''
    errorList = [] # 错误信息

    # 有空行
    blankRowNoList = readerObj.getBlankRowNoList()
    if blankRowNoList:
        setError(True)
        errorList.append("空行检查:{}".format(blankRowNoList))
    
    # 有重复id
    duplicateIdList = readerObj.getDuplicateIdList()
    if duplicateIdList:
        setError(True)
        errorList.append("重复id检查:{}".format(",".join(duplicateIdList)))
    
    for checkerObj in checkerList:
        try:
            checkerObj.checkData(readerObj)
            errorInfo = checkerObj.formatErrorInfo()
            if errorInfo: # 有错误
                setError(True)
                errorList.append(errorInfo)
        except:
            setError(True)
            log.log("导表检查错误, checker:{},fileName:{}", printInfo.printClassInfo(checkerObj), fileName)
            traceback.print_exc()
            return
    
    if errorList:
        log.log("{}\n".format("-" * 40))
        error = "导表:{}\n{}\n\n".format(fileName, "\n".join(errorList))
        log.log(error)
    
        
def checkDuplicateId():
    '''检查重复id
    '''
    for patternList in config.joinFileList:
        readerList = []
        for fileName, readerObj in gTableList.items():
            for pattern in patternList:
                if re.match(pattern, fileName):
                    readerList.append(readerObj)
        if readerList:
            doCheckDuplicateId(patternList, readerList)
            
def doCheckDuplicateId(patternList, readerList):
    idList = {}
    for readerObj in readerList:
        for rowNo, fieldObj in readerObj.iterColData(1):
            idValue = fieldObj.value
            fieldList = idList.setdefault(idValue, [])
            fieldList.append(fieldObj)
    
    errorList = []
    for idValue, fieldList in idList.items():
        if len(fieldList) > 1:
            data = {}
            for fieldObj in fieldList:
                fileName = fieldObj.fileName
                rowNoList = data.setdefault(fileName, [])
                rowNoList.append(str(fieldObj.rowNo))
            
            lst = []
            for fileName, rowNoList in data.items():
                lst.append("\t\t导表:{}\n\t\t　　行号:{}".format(fileName, ",".join(rowNoList)))        
            errorList.append("重复id:{}\n{}\n".format(idValue, "\n".join(lst)))
    
    if errorList:
        log.log("{}\n".format("-" * 40))
        log.log("关联检查:{}\n{}\n\n", patternList, "".join(errorList))

       
def setError(error):
    '''设置是否有错误
    '''
    global gError
    if error:
        gError = True
    else:
        gError = False
        
def isErorr():
    global gError
    return gError

def isIgnoreFile(fileName):
    '''是否忽略文件
    '''
    for pattern in config.ignoreFileList:
        if re.match(pattern, fileName):
            return True
    return False


import re
import reader
import checker
import log
import traceback
import config
from utils import printInfo

if "gTableList" not in globals():
    global gTableList, gError
    gTableList = {}
    gError = False
