import functools
import time
from functools import reduce, wraps


def add(x, y, f):
    return f(x) + f(y)

def f1(x):
    return x * x

def add2(x, y):
    return x + y

def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def normalize_name(name):
    name = name.strip()
    if not name:
        return ''  # 如果是空字符串就直接返回空
    return name[0].upper() + name[1:].lower()

def is_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    # =============================高阶函数=============================
    # 编写高阶函数，就是让函数的参数能够接收别的函数。
    print(abs(-10))
    # 要获得函数调用结果，我们可以把结果赋值给变量
    x = abs(-10)
    print(x)

    # 如果把函数本身赋值给变量呢？
    f = abs
    print(f)
    # 结论：函数本身也可以赋值给变量，即：变量可以指向函数。

    # 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数
    print(f(-10))

    # 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
    # 传入函数
    x = -5
    y = 6
    f = abs
    print(add(x, y, f))

    # =============================map/reduce=============================
    # map生成generator
    r = map(f1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))


    print(list(map(f1, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

    # resuce 归约
    print(reduce(add2, [1, 3, 5, 7, 9]))

    print(reduce(fn, map(char2num, '13579')))

    # 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
    names = ['adam', 'LISA', 'barT']
    print(list(map(str.capitalize, names)))

    print(list(map(normalize_name, names)))


    # =============================filter=============================
    # 在一个list中，删掉偶数，只保留奇数
    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

    # =============================sorted=============================
    print(sorted([36, 5, -12, 9, -21]))
    print(sorted([36, 5, -12, 9, -21], key=abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


    # =============================返回函数=============================
    # 实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
    def calc_sum(*args):
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    # 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax

        return sum


    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)

    print(f())

    # =============================匿名函数=============================
    # 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
    L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(L)

    # 把匿名函数作为返回值返回
    def build(x, y):
        return lambda: x * x + y * y


    def is_odd(n):
        return n % 2 == 1

    L1 = list(filter(is_odd, range(1, 20)))
    print(L1)
    L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
    print(L2)

    # =============================装饰器=============================
    # 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
    def now():
        print('2024-6-1')

    f4 = now
    # f4()

    # 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字

    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)

        return wrapper


    # 把@log放到now()函数的定义处，相当于执行了语句： now = log(now)
    @log
    def now():
        print('2024-6-1')


    now()


    def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator

    # 两层嵌套的decorator相比，3层嵌套的效果是这样的： now = log('execute')(now)
    @log('execute')
    def now():
        print('2024-6-1')

    now()


    # 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()  # 记录开始时间
            result = func(*args, **kwargs)  # 执行原函数
            end_time = time.time()  # 记录结束时间
            print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.6f} 秒")
            return result  # 返回原函数结果

        return wrapper


    @timer
    def test_sleep(n):
        """休眠 n 秒"""
        time.sleep(n)
        return f"Slept {n} seconds"

    print(test_sleep(2))


    # =============================偏函数=============================
    print(int('12345'))
    # int()函数提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
    print(int('12345', base=8))


    def int2(x, base=2):
        return int(x, base)

    # functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
    int2 = functools.partial(int, base=2)
    print(int2('1000000'))