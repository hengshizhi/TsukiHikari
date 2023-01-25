# TsukiHikari
一个pythonweb框架，给自己方便使用的,平时没事可以拿来玩
<br>启动命令:python app.py
<h1>下面是文档啊</h1>
<br>首先,这是一个web服务器,直接运行`app.py`文件就可以启动,然后可以根据需要设置WWWROOT根路径
<br>在项目的wwwroot下面有一个示例文件:`index.py`,这个文件就相当于web服务器的php文件,访问直接运行
比如`http://127.0.0.1:8888/index.py`
会看的应该可以看到,代码里面开头有一串导入文件,这堆import不是必须的,根据需要选择,python会缓存import的文件
````
import KamitaTomoe.output as output
import KamitaTomoe.html as html
import KamitaTomoe.gain as gain
import KamitaTomoe.session as session
````
然后我看也可以看见一个在当前文件未被定义的函数`chdir()`
这个函数至关重要,在导入 KamitaTomoe 库之后必须使用这个函数,否则可能会在某些需要文件操作的地方报错
(包括import自定义库),因为这个函数他负责切换python的运行路径
然后会看到`os.chdir(session._root)`,这个不需要管他,这个切换工作路径是为了使用session,因为只有在项目根路径(即`app.py`的路径才可以使用session,现在原因未知,列如BUG列表,会善后解决)
