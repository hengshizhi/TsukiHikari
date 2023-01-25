# TsukiHikari
一个pythonweb框架，给自己方便使用的,平时没事可以拿来玩,做一点小项目<br>
本项目基于flask框架,所以也就自然支持其他web服务器的部署<br>
启动命令:python app.py<br>
# 下面是文档啊
## 一个例子
首先,这是一个web服务器,直接运行`app.py`文件就可以启动,然后可以根据需要设置WWWROOT根路径<br>
在项目的wwwroot下面有一个示例文件:`index.py`,这个文件就相当于web服务器的php文件,访问直接运行<br>
比如`http://127.0.0.1:8888/index.py`<br>
会看的应该可以看到,代码里面开头有一串导入文件,这堆import不是必须的,根据需要选择,python会缓存import的文件<br>
````
import KamitaTomoe.output as output
import KamitaTomoe.html as html
import KamitaTomoe.gain as gain
import KamitaTomoe.session as session
````
然后我看也可以看见一个在当前文件未被定义的函数`chdir()`<br>
这个函数至关重要,在导入 KamitaTomoe 库之后必须使用这个函数,否则可能会在某些需要文件操作的地方报错<br>
(包括import自定义库),因为这个函数他负责切换python的运行路径<br>
然后会看到`os.chdir(session._root)`,这个不需要管他,这个切换工作路径是为了使用session,因为只有在项目根路径(即`app.py`<br>的路径才可以使用session,现在原因未知,列如BUG列表,会善后解决,提示:已经解决了,如果使用session,在文件末尾必须执行session.move()方法)<br>
然后会看到下面的代码<br>
````
if(gain.posts('user') == 'shizhi' and gain.posts('password') == '123'):
    output.echo('''登陆成功''')
else:
    output.echo('''.....(省略号)''')
````
可以看到,这里output.echo复刻了php`echo`函数的功能,他的作用就是给网页输出东西,他有两个参数如下:<br>
`content,MIME='text/html'`,第一个自然是输出的内容,支持几乎可以输出的所有格式(文本/二进制)<br>
第二个参数是MIME类型,懂得都懂,不会自学出门左转搜索引擎<br>
这里还有一个`gain.posts('user') `方法,这个方法传入值是一个字符串,查找POST请求的字段,一般用于表单接收,同类型方法还有:<br>
`gain.gets`,目前只做了最常用的两种<br>
# 方法大全
## output
````
headers(headers_c:dict)
'''自定义请求头:headers_c:请求头,例子{'Cache-Control':'max-age=0'}'''

redirect(url:str,code:int = 301)
'''重定向:url:重定向之后的URL,code:301或者302'''

echo (content,MIME='text/html'): #优先级 非html>html
    '''优先级 非html>html,content->内容'''
Web_output(output:bool = False):
    '''output:是否输出
    真:输出，假:只返回
    '''
#Web_output给web服务器调用的接口
'''Web_output接口文档
返回示例:s{'content': '' , 'MIME' : 'text/html','headers':{'xxx':'xxx'},'redirect':None}
content为内容,返回的内容
MIME为返回的类型
headers为请求头
redirect:默认为None,如果被修改则是[url,301/302]为重定向,重定向的URL,如果有重定向,就不会返回内容
'''

````
## gain
````
get() -> dict #获取所有的GET参数
post() -> dict #获取所有POST参数
headers() -> dict #获取所有头部信息
gets(s) -> bool or None #根据请求的键获取值
posts(s) -> bool or None
````
## session
````
_root = None #项目根路径
File_path = None #文件路径
session = dict #会话的字典,需要更改session可以直接更改里面的值
getdict() -> dict:
    '''获取所有session'''
sessions(s:str):
    '''获取session'''
modify(m:dict):
    '''修改session'''
move()#无参数,使用session的话在代码末尾必须要调用这个函数
````
