#kt语言驱动
import subprocess,json
kt = './Kamita_Tomoe/KamitaTomoe.py'
def kt_go(Execution_file_path:str) -> dict:
    '''传入要执行的kt文件路径
    输出：{'content': '<返回的内容(包括html等)>', 'MIME': '<返回的MIME类型>'}
    '''
    GBK = 'gbk'
    UTF8 = 'utf-8'

    # 解码方式，一般 py 文件执行为utf-8 ，cmd 命令为 gbk
    current_encoding = GBK
    # 构造popen
    popen = subprocess.Popen(f'python ./Kamita_Tomoe/KamitaTomoe.py --file {Execution_file_path}', shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines=True,
                            bufsize = 1)       
    # 执行                                           
    out,err = popen.communicate()
    return json.loads(out)
#print(kt_go('D:\Downloads\TsukiHikari\wwwroot/ktgongs/index.kt'))