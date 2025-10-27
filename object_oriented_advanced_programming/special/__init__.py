from enum import Enum

from object_oriented_advanced_programming.Weekday import Weekday
from object_oriented_advanced_programming.special.Fib import Fib
from object_oriented_advanced_programming.special.Student import Student

if __name__ == '__main__':

    # __str__()

    print(Student('CJH'))
    # <object_oriented_advanced_programming.special.Student.Student object at 0x000001C3CD421160>
    # 打印出一堆<object_oriented_advanced_programming.special.Student.Student object at 0x000001C3CD421160>，不好看

    # 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
    # Student object (name: CJH)
    s = Student('CJH')
    print(s)

    # __iter__
    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    # 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
    # Fib 在未实现__iter__、__next__时 会报错 因为无法迭代
    for n in Fib():
        print(n)

    # __getitem__
    # Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行 要重写__getitem__
    #  f = Fib() 仅使用 f[n]时  可以不用重写__iter__ 和 __next__
    f = Fib()
    print(f[0])
    print(f[1])
    print(f[2])
    print(f[10])

    # f切片 切片报错
    print(f[0:5])
    # 对于Fib切片报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice

    # __getitem__要重写判断
    # 正常了
    print(f[0:5])


    # __getattr__ 在没有找到属性的情况下，会调用__getattr__
    # 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
    s = Student("cjh")
    print(s.name)

    # 报错 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
    print(s.score)

    # 也可以返回函数
    print(s.age())

    # None
    # print(s.abc)

    # 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
    # print(s.abc)
    # AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # __call__
    # 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()可以直接在实例本身上调用
    s2 = Student('CJH')
    s2()

    # 相当于 __call__ 会把一个类 变成方法 并且 默认的逻辑就在__call__中编写

    # 枚举类
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

    # 访问枚举
    day1 = Weekday.Mon
    print(day1)

    print(Weekday.Tue)

    print(Weekday.Tue.value)

    print(day1 == Weekday.Mon)

    print(day1 == Weekday.Tue)

    print(day1 == Weekday(1))

    print(day1 == Weekday(0))