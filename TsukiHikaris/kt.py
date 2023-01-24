#kt语言驱动
import subprocess,json,base64
from flask import Response,abort,request
import os
import sys
def get(): #获取所有的GET参数
    return request.args.to_dict()
kt = '/root/RemoteWorking/python-cloud-studio-demo/KamitaTomoek' #绝对路径
root = '/root/RemoteWorking/python-cloud-studio-demo/' #项目根路径
sys.path.append('/root/RemoteWorking/python-cloud-studio-demo/KamitaTomoek')
os.chdir(kt)
import main as KtMain
import KamitaTomoe.session as session
session._root = root
os.chdir(root)
def strToBase64(s):
    '''
    将字符串转换为base64字符串
    :param s:
    :return:
    '''
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')
def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding='gbk'))
    return str(strDecode, encoding='gbk')
def ktpy(Execution_file_path=None):
    os.chdir(kt)
    move = KtMain.move(Execution_file_path,root)
    session.File_path = Execution_file_path
    os.chdir(root)
    ret = {'return':move.output()}
    ret.update(move._output)
    move = None
    return ret