def Import(file,code='utf-8'):
    try:
        return open(file=file,encoding=code)
    except:
        return None