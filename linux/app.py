# -*- coding: UTF-8 -*-
#import AutoInstall
# 导入Flask类
from flask import Flask,Response,abort
#导入MIME判断
import MIME
import os
import kt
import sys
import json
# import sys
# import time

Whether_to_return_status_code_at_404 = True
WWWROOT = 'wwwroot/'
INDEX = \
[
'index.kt',
'index.py',
'index.html',
'index.htm',
'default.py',
'default.html',
'default.html',
'404.py',
'404.html',
'404.htm',
'404'
]


def interpreter(File_path,Extension): #web服务器特定代码文件的解释器
    if(Extension in ['py','kt']):
        pass #执行解释器
def INDEX_File_exists(catalogue,INDEX = INDEX):
    '''传入目录,返回有文件的目录'''
    if(catalogue != ''):
        if(catalogue[len(catalogue)-1] != '/'):
            if(os.path.isfile(WWWROOT+catalogue)): #判断文件是否存在
                return WWWROOT+catalogue
            else:
                catalogue += '/'
        #print('aaaashuaguynzhn')
        # if('.' in  catalogue.split('/')[len(catalogue.split('/'))-2]):
        #     return WWWROOT+catalogue        
    for i in INDEX:  #扫码访问的本目录
        if(os.path.isfile(WWWROOT+catalogue+i)): #判断文件是否存在
            if('404' in i and Whether_to_return_status_code_at_404):
                abort(404)
            return WWWROOT+catalogue+i
    INDEX = \
    [
    '404.py',
    '404.html',
    '404.htm',
    '404'
    ] #更改要扫描的根目录内容
    for i in INDEX: #扫码根目录
        if(os.path.isfile(WWWROOT+i)): #判断文件是否存在
            if('404' in i and Whether_to_return_status_code_at_404):
                abort(404)
            return WWWROOT+i
    raise Exception('不存在这样的文件或目录')
def Return_content(catalogue):
    catalogue = INDEX_File_exists(catalogue)
    file_extension = os.path.splitext(catalogue)[-1][1:]
    _MIME_is_MIME = MIME._MIME(file_extension) #_MIME函数根据文件后缀猜出来的MIME类型
    if(_MIME_is_MIME != '' and file_extension != 'kt'):
        return Response(open(catalogue,mode='rb'), mimetype=_MIME_is_MIME)
    elif(file_extension == 'kt'):
        neir = json.loads(json.loads(kt.kt_go(catalogue))[0]) #调用kt解释器
        return Response(neir['content'], mimetype=neir['MIME'])
    else:
        return Response(open(catalogue,mode='rb'), mimetype='text/plain')
    abort(500)
    return Response('出大错误了', mimetype='text/plain')
# Flask函数接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)
# 装饰器的作用是将路由映射到视图函数 index
@app.route('/')
def index_root():
    return Return_content('/')
@app.route('/<path:catalogue>')
def index_NoRoot(catalogue):
    return Return_content(catalogue)
@app.route('/favicon.ico')#设置icon
def favicon():
    return 'no'
# Flask应用程序实例的 run 方法 启动 WEB 服务器
if __name__ == '__main__':
    #app.run()    # 可以指定运行的主机IP地址，端口，是否开启调试模式
    app.run(host="0.0.0.0", port=9000, debug = True)