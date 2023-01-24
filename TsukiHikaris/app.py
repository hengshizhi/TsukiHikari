#import AutoInstall
# 导入Flask类
from flask import Flask,Response,abort,request
#导入MIME判断
import MIME
import os
import kt
import sys
# import sys
# import time
Load_mod = 'mod' #/<path:catalogue>/<Load_mod>/<path:modn> ,加载mod的时候的中间路径
Whether_to_return_status_code_at_404 = True
WWWROOT = './wwwroot/'
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

def INDEX_File_exists(catalogue:str,INDEX:list = INDEX) -> str:
    '''传入目录,返回有文件的目录'''
    if(catalogue != ''):
        if(catalogue[len(catalogue)-1] != '/'):
            if(os.path.isfile(WWWROOT+catalogue)): #判断文件是否存在
                return WWWROOT+catalogue
            else:
                catalogue += '/'    
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
    #raise Exception('不存在这样的文件或目录')
def Return_content(catalogue,format = 'Response'):
    '''catalogue:目录参数,对应下文的<path:catalogue>
    format:返回格式,支持Response或者content,Response时返回<Response>,<响应状态>,<请求头>,否则返回文件内容list[<内容>,<MIME>]'''
    catalogue = INDEX_File_exists(catalogue)
    file_extension = os.path.splitext(catalogue)[-1][1:]
    _MIME_is_MIME = MIME._MIME(file_extension) #_MIME函数根据文件后缀猜出来的MIME类型
    if(_MIME_is_MIME != '' and file_extension != 'py'):
        if(format == 'Response'):
            return Response(open(catalogue,mode='rb'), mimetype=_MIME_is_MIME),200,{}
        else:
            return [open(catalogue,mode='rb').read(),_MIME_is_MIME]
    elif(file_extension == 'py'):
        neir = kt.ktpy(catalogue) #调用kt包
        if(format == 'Response'):
            return neir['return']
        else:
            del neir['return']
            return neir
    else:
        if(format == 'Response'):
            return Response(open(catalogue,mode='rb'), mimetype='text/plain'),200,{}
        else:
            return [open(catalogue,mode='rb').read(),'text/plain']
    abort(500)
    return Response('出大错误了', mimetype='text/plain')
def mod(catalogue,modn): #加载mod
    '''参数：
    catalogue : str 文件路径<path:catalogue>
    modn : str mod的名字
    return:
    Response对象,可以直接当作app.route装饰器下的函数返回值
    mod开发标准:
    app.py会自动调用mod的main函数,必须要main函数作为入口函数,函数传值:
    catalogue：访问文件的目录（str），RC：访问文件的内容（list[<文件内容>,<MIME>])
    返回值：->list['输出内容','MIME']
    '''
    RC = Return_content(catalogue,False)  #获取访问文件内容
    catalogue = WWWROOT+catalogue #拼接完整路径
    mod = __import__(f'mod.{modn}',RC) #导入mod包
    exec(f'mods = mod.{modn}.main(catalogue,RC)') #运行mod
    mod = locals()['mods'] #获取mod返回值
    return Response(mod[0], mimetype=mod[1])
def get(): #获取所有的GET参数
    return request.args.to_dict()
def post(): #获取所有POST参数
    return request.values.to_dict()
# Flask函数接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)
# 装饰器的作用是将路由映射到视图函数 index
@app.route('/',methods=['GET','POST'])
def index_root():
    return Return_content('/')
@app.route(f'/<path:catalogue>/{Load_mod}/<path:modn>',methods=['GET','POST'])
def index_mod(catalogue,modn):
    return mod(catalogue,modn)
@app.route(f'/{Load_mod}/<path:modn>',methods=['GET','POST'])
def index_mod_root(modn):
    return mod('/',modn)
@app.route('/favicon.ico',methods=['GET','POST'])#设置icon
def favicon():
    return 'no'
@app.route('/<path:catalogue>',methods=['GET','POST'])
def index_NoRoot(catalogue):
    return Return_content(catalogue)
# Flask应用程序实例的 run 方法 启动 WEB 服务器
if __name__ == '__main__':
    #app.run()    # 可以指定运行的主机IP地址，端口，是否开启调试模式
    app.secret_key = "affedasafafqwe"
    app.run(host="0.0.0.0", port=8888, debug = False)