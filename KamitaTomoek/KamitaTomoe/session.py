from flask import session as flaskse
import os
_root = None #项目根路径
File_path = None #文件路径
session = flaskse #缓存已经修改的session
def getdict() -> dict:
    '''获取所有session'''
    return dict(session)
def sessions(s:str):
    '''获取session'''
    try:r = session[s]
    except:r = None
    return r
def modify(m:dict):
    '''修改session'''
    os.chdir(_root)
    for k,v in m.items():session[k] = v
def move(): #到代码运行结尾运行move修改flask上的session
    '''运行session修改,注意(很重要):'''
    os.chdir(_root)
    for k,v in session.items():
        flaskse[k] = v
    session = {}
