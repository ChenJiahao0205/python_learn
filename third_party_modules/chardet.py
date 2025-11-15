from requests.compat import chardet

if __name__ == '__main__':
    # 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。
    # 虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，
    # 但是，在不知道编码的情况下，对bytes做decode()不好做

    # 安装chardet
    # 如果安装了Anaconda，chardet就已经可用了。否则，需要在命令行下通过pip安装
    # pip install chardet

    # 使用chardet
    # 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码
    c = chardet.detect(b'Hello, world!')
    print(c)

    # 我们来试试检测GBK编码的中文
    data = '离离原上草，一岁一枯荣'.encode('gbk')
    c = chardet.detect(data)
    print(c)

    data = '离离原上草，一岁一枯荣'.encode('utf-8')
    c = chardet.detect(data)
    print(c)

    # 再试试对日文进行检测
    data = '最新の主要ニュース'.encode('euc-jp')
    c = chardet.detect(data)
    print(c)