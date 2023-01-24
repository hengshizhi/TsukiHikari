import json
echo_c = {'content': '' , 'MIME' : 'text/html','headers':{},'redirect':None}
def headers(headers_c:dict):
    '''自定义请求头:headers_c:请求头,例子{'Cache-Control':'max-age=0'}'''
    echo_c['headers'].update(headers_c) 
def redirect(url:str,code:int = 301):
    '''重定向:url:重定向之后的URL,code:301或者302'''
    echo_c['redirect'] = [url,code]
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
    global echo_c
    if(output == True):
        print(f'content -> {echo_c["content"]}\nMIME -> {echo_c["MIME"]}')
    s = echo_c
    echo_c = {'content': '' , 'MIME' : 'text/html','headers':{},'redirect':None}
    return s
#Web_output给web服务器调用的接口
'''Web_output接口文档
返回示例:s{'content': '' , 'MIME' : 'text/html','headers':{'xxx':'xxx'},'redirect':None}
content为内容,返回的内容
MIME为返回的类型
headers为请求头
redirect:默认为None,如果被修改则是[url,301/302]为重定向,重定向的URL,如果有重定向,就不会返回内容
'''