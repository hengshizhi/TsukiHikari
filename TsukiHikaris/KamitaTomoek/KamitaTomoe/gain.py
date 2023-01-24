from flask import Response,abort,request

def get() -> dict(): #获取所有的GET参数
    return request.args.to_dict()
def post() -> dict(): #获取所有POST参数
    return request.values.to_dict()
def headers() -> dict(): #获取所有头部信息
    return dict(request.headers)
def gets(s) -> bool or None:
    try:return request.args.to_dict()[s]
    except:return None
def posts(s) -> bool or None:
    try:return request.values.to_dict()[s]
    except:return None