# -*- coding: UTF-8 -*-
import os
from flask import Response,request
class move:
    FilePath = ''
    FileContent = None
    Response = None #Response对象
    HTTPstate = 200 #HTTP状态
    header = {} #响应头
    def __init__(self,FilePath:str,root:str):
        '''文件路径,项目根路径'''
        try:
            self.FilePath = FilePath
            self.FileContent = open(file='../'+FilePath, mode='r',encoding='utf-8').read()
        except:
            self.Response=Response('<h1>404</h1>',mimetype='text/html')
            self.HTTPstate = 404
            return None
        exec('import os\n'+f'def chdir():os.chdir(\'.{os.path.dirname(self.FilePath)}\')\n'+self.FileContent+'\n_output = output.Web_output()',globals())
        self._output = _output
        if(_output['redirect'] != None):
            self.Response = request(_output['redirect'][0],_output['redirect'][1])
            self.HTTPstate = _output['redirect'][1]
        else:
            self.Response = Response(_output['content'],mimetype=_output['MIME'])
            self.HTTPstate = 200
            self.header = _output['headers']
    def output(self):
        return self.Response,self.HTTPstate,self.header