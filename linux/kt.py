# -*- coding: UTF-8 -*-
#kt语言驱动
import subprocess,json
kt = './Kamita_Tomoe/KamitaTomoe.py'
def kt_go(Execution_file_path):
    '''传入要执行的kt文件路径
    输出：{'content': '<返回的内容(包括html等)>', 'MIME': '<返回的MIME类型>'}
    '''
    # 构造popen
    #print('python ./Kamita_Tomoe/KamitaTomoe.py --file '+Execution_file_path)
    popen = subprocess.Popen('python ./Kamita_Tomoe/KamitaTomoe.py --file '+Execution_file_path, shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines=True,
                            bufsize = 1)       
    # 执行                                           
    out = popen.communicate()
    return json.dumps (out)
#print(json.loads(kt_go('wwwroot/ktgongs/index.kt'))[0])