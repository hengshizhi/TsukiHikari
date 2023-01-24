## 欢迎来到 Cloud Studio ##

这是一个展现 Cloud Studio 功能的 Python 示例。

##  自动预览 ##

之所以自动运行了这个应用并打开了预览窗口，是因为有 `.vscode/preview.yml` 文件存在。

该文件的格式说明如下：

```yml
# .vscode/preview.yml
autoOpen: false
apps:
  - port: 5000
    run: 'pip install -i https://mirrors.tencent.com/pypi/simple/ -r ./requirements.txt && python ./app.py'
    root: ./web
    name: Python Cloud Studio Demo
    description: Python Cloud Studio Demo Project
    autoOpen: true

```

### 生成预览配置文件 ###
如果你想生成该文件，可以按下 <kbd>CMD+Shift+P</kbd>，打开命令面板，输入 `preview`，在命令列表中点击 **Preview: Generate Preview Config File**。

### 启动预览窗口 ###
有了这个文件后，你可以自己启动预览窗口。按下 <kbd>CMD+Shift+P</kbd>，打开命令面板，输入 `preview`，在命令列表中点击 **Preview: Open Preview Tab**。

##  手动开启预览调试 ##

1. 先进入到 `web` 目录，然后在终端直接运行 `pip install -i https://mirrors.tencent.com/pypi/simple/ -r ./requirements.txt && python ./app.py` 启动服务。

2. 完全启动之后，打开命令面板(`Command + Shift + P` 或 `Ctrl + Shift + P`) 并输入 `open preview tab`, 回车。

![](./static/img2.png)

3. 输入端口号 `5000`，回车后将自动打开预览窗口。
