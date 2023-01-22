import json
echo_c = {'content': '' , 'MIME' : 'text/html'}
def echo (content,MIME='text/html'): #优先级 非html>html
    '''优先级 非html>html,content->内容'''
    if(echo_c['MIME'] == MIME):
        echo_c['content'] += content
    else:
        echo_c['content'] = content
        echo_c['MIME'] = MIME
    return type(content)
def Web_output(output:bool = False):
    '''output:是否输出
    真:输出，假:只返回
    '''
    if(output == True):
        print(f'content -> {echo_c["content"]}\nMIME -> {echo_c["MIME"]}')
    return json.dumps(echo_c)
#Web_output给web服务器调用的东西
