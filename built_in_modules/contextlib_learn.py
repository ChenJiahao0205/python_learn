from contextlib import contextmanager, closing
from urllib.request import urlopen

from built_in_modules.Query import Query
from built_in_modules.Query2 import create_query2

if __name__ == '__main__':
    # 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
    try:
        f = open('C:/Users/Administrator/Desktop/test.txt', 'r')
        f.read()
    finally:
        if f:
            f.close()

    # 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
    with open('C:/Users/Administrator/Desktop/test.txt', 'r') as f:
        f.read()

    # 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句

    # 实现上下文管理是通过__enter__和__exit__这两个方法实现的
    with Query('CJH') as q:
        q.query()

    # @contextmanager
    # 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法
    with create_query2('cjh') as q:
        q.query()

    # 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用 @ contextmanager实现。例如：
    @contextmanager
    def tag(name):
        print("<%s>" % name)
        yield
        print("</%s>" % name)

    with tag("h1"):
        print("hello")
        print("world")

    # 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)
    # closing也是一个经过__enter__和__exit__