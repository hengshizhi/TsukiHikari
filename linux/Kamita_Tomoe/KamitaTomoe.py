# -*- coding: UTF-8 -*-
import sys
import getopt
import os
class move:
    Final_code = '' #最后生成的代码
    def __init__(self): 
        self.file_content = open(file,mode='r').read() #读取文件
        luj = '/'.join(file.split('/')[0:-1])  #更换运行路径
        self.parse() #语法分析
        self.Final_code = '\n'.join(['import KamitaTomoe.'+i+' as '+i for i in ['output','html']])+'\n' \
        +'import os \nos.chdir(\''+luj+'\')' \
        +self.Final_code.replace('import KamitaTomoe.output as output','').replace('import KamitaTomoe.html as html','')
        self.Final_code += '\nprint(output.Web_output())' #返回生成的HTML
    def Program_parse(self,code): #程序代码部分语法分析
        self.Final_code += (code+'\n')
    def parse(self): #语法分析
        '''语法解析'''
        code =[i.split('%>') for i in self.file_content.split('<%')][1:] #list[list['程序代码','html代码']]
        for i in code:
            for i1 in range(2):
                if(i1 == 0): #执行程序代码
                    self.Program_parse(i[0])
                else:
                    self.Final_code += 'output.echo(\'\'\''+i[1]+'\'\'\')\n'
if __name__ == '__main__':
    file = ''.join(getopt.getopt(sys.argv[1:],'-f',['file'])[1])
    Extension = file.split('.')[-1]
    if(Extension != 'py' and Extension != 'kt'): #判断扩展名
        print('Illegal file format')
    else:
        try:
            moves = move()
            exec(moves.Final_code) #运行代码
        except Exception as e:
            print('Exception:', e)
        except: #如果不传入文件，那就使用交互式
            print('已经对交互式编程停止支持')
