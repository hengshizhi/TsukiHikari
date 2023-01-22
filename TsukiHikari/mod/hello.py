def main(catalogue,RC)->list: #->list['输出内容','输出MIME']
    a = f'''欢迎使用mod!你的页面的内容是{RC[0].decode('utf-8')}'''
    return [a,'text/html']