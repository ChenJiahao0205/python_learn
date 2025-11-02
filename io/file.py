if __name__ == '__main__':
    # ======================读文件======================
    #  r表示只读
    f = open('C:/Users/Administrator/Desktop/test.txt', 'r')

    try:
        f_not_exist = open('C:/Users/Administrator/Desktop/error.txt', 'r')
    except FileNotFoundError as e:
        print('No such file or directory: C:/Users/Administrator/Desktop/error.txt')

    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    print(f.read())

    # 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
    f.close()

    # 正确读取和关闭的方式
    try:
        f = open('C:/Users/Administrator/Desktop/test.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()

    # 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
    with open('C:/Users/Administrator/Desktop/test.txt', 'r') as f:
        print(f.read())

    # try read finally close 和 with read 效果是一样的

    # ======================file-like Object======================
    # 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
    f2 = open('C:/Users/Administrator/Desktop/e98afb616614a4c7146c1d3eb776459.png', 'rb')
    # 十六进制表示的字节
    print(f2.read())
    f2.close()

    # ======================字符编码======================
    f3 = open('C:/Users/Administrator/Desktop/test.txt', 'r', encoding='utf-8')
    print(f3.read())
    f3.close()

    # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
    f4 = open('C:/Users/Administrator/Desktop/test.txt', 'r', encoding='utf-8', errors='ignore')
    f4.close()

    # ======================写文件======================
    # 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
    f5 = open('C:/Users/Administrator/Desktop/test.txt', 'w')
    f5.write('cover world')
    f5.close()

    f6 = open('C:/Users/Administrator/Desktop/test.txt', 'r')
    f6.read()
    f6.close()

    # 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险
    # 在写write的时候 一定要调用close 感觉很像flush

    f7 = open('C:/Users/Administrator/Desktop/test.txt', 'a')
    f7.write('append world')
    f7.close()

    f8 = open('C:/Users/Administrator/Desktop/test.txt', 'r')
    f8.read()
    f8.close()

    # 使用with操作文件是个好习惯 尽可能地使用with
