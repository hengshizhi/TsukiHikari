from flask import session
import os
_root = None #项目根路径
File_path = None #文件路径
def getdict() -> dict:
    '''获取所有session'''
    r = session
    return dict(r)
def sessions(s:str):
    '''获取session'''
    try:r = session[s]
    except:r = None
    return r
def modify(m:dict):
    '''修改session'''
    os.chdir(_root)
    for k,v in m.items():session[k] = v