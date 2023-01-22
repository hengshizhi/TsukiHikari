class content():
    structure = []
    def __init__(self,html_content) -> None:
        self.html = html_content
        self.analysis()
class Import():
    def __init__(self,file,code='utf-8') -> None:
        file = open(file=file,encoding=code).read ()
        self.content = content(file)