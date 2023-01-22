#import AutoInstall
# 导入Flask类
from flask import Flask,Response,abort
#导入MIME判断
import MIME
import os
import kt
import sys
# import sys
# import time
Load_mod = 'mod' #/<path:catalogue>/<Load_mod>/<path:modn> ,加载mod的时候的中间路径
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


def interpreter(File_path:str,Extension): #web服务器特定代码文件的解释器
    if(Extension in ['py','kt']):
        pass #执行解释器
def INDEX_File_exists(catalogue:str,INDEX:list = INDEX) -> str:
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
def Return_content(catalogue,format = 'Response'):
    '''catalogue:目录参数,对应下文的<path:catalogue>
    format:返回格式,支持Response或者content,Response时返回Response对象,否则返回文件内容list[<内容>,<MIME>]'''
    catalogue = INDEX_File_exists(catalogue)
    file_extension = os.path.splitext(catalogue)[-1][1:]
    _MIME_is_MIME = MIME._MIME(file_extension) #_MIME函数根据文件后缀猜出来的MIME类型
    if(_MIME_is_MIME != '' and file_extension != 'kt'):
        if(format == 'Response'):
            return Response(open(catalogue,mode='rb'), mimetype=_MIME_is_MIME)
        else:
            return [open(catalogue,mode='rb').read(),_MIME_is_MIME]
    elif(file_extension == 'kt'):
        neir = kt.kt_go(catalogue) #调用kt解释器
        print(neir)
        if(format == 'Response'):
            return Response(neir['content'], mimetype=neir['MIME'])
        else:
            return [neir['content'],neir['MIME']]
    else:
        if(format == 'Response'):
            return Response(open(catalogue,mode='rb'), mimetype='text/plain')
        else:
            return [open(catalogue,mode='rb').read(),'text/plain']
    abort(500)
    return Response('出大错误了', mimetype='text/plain')
def mod(catalogue,modn):
    RC = Return_content(catalogue,False) 
    catalogue = WWWROOT
    mod = __import__(f'mod.{modn}',RC)
    exec('mods = mod.hello.main(catalogue,RC)')
    mod = locals()['mods']
    return Response(mod[0], mimetype=mod[1])


# Flask函数接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)
# 装饰器的作用是将路由映射到视图函数 index
@app.route('/')
def index_root():
    return Return_content('/')
@app.route(f'/<path:catalogue>/{Load_mod}/<path:modn>')
def index_mod(catalogue,modn):
    return mod(catalogue,modn)
@app.route(f'/{Load_mod}/<path:modn>')
def index_mod_root(modn):
    return mod('/',modn)
@app.route('/favicon.ico')#设置icon
def favicon():
    return 'no'
@app.route('/<path:catalogue>')
def index_NoRoot(catalogue):
    return Return_content(catalogue)
# Flask应用程序实例的 run 方法 启动 WEB 服务器
if __name__ == '__main__':
    #app.run()    # 可以指定运行的主机IP地址，端口，是否开启调试模式
    app.run(host="0.0.0.0", port=8888, debug = True)