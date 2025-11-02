from io import StringIO, BytesIO

if __name__ == '__main__':
    # StringIO
    # 很多时候，数据读写不一定是文件，也可以在内存中读写
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world')

    # getvalue()方法用于获得写入后的str
    print(f.getvalue())

    # 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        oneLine = f.readline()
        if oneLine == '':
            break
        print(oneLine.strip())

    # BytesIO
    # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
    f2 = BytesIO()
    f2.write('中文'.encode('utf-8'))
    # b'\xe4\xb8\xad\xe6\x96\x87'
    print(f2.getvalue())

    # 可以用一个bytes初始化BytesIO，然后，像读文件一样读取
    f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(f3.read())