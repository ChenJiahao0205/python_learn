import json
import pickle

if __name__ == '__main__':
    # 序列化
    # 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict
    # d = dict(name='Bob', age=20, score=88)

    # 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'
    # 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
    # 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
    # Python提供了pickle模块来实现序列化。

    # 首先，我们尝试把一个对象序列化并写入文件
    d = dict(name='Bob', age=20, score=88)
    s = pickle.dumps(d)
    print(s)

    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()

    # 反序列化
    f2 = open('dump.txt', 'rb')
    d = pickle.load(f2)
    # {'name': 'Bob', 'age': 20, 'score': 88}
    # 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
    print(d)
    f2.close()

    # JSON 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式

    # JSON类型           Python类型
    # {}                dict
    # []                list
    # "string"          str
    # 1234.56           int或float
    # true / false      True / False
    # null              None

    # Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
    d2 = dict(name='Bob', age=20, score=88)
    j = json.dumps(d2)
    print(j)

    # 反序列化
    print(json.loads(j))


    class Student(object):
        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score

    # 这个方法 要么写在 class外面 然后下方使用student2dict去传入
    # 要么写在class里面 把student2dict变为静态方法(将方法改为静态方法（无需访问实例属性） 需要加装饰 @staticmethod) 下方使用Student.student2dict去传入
    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

    # Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
    s3 = Student('Bob', 20, 88)
    # 这么写会报错 因为Student目前是一个不可序列化的对象
    # print(json.dumps(s3))

    # dumps 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
    print(json.dumps(s3, default=student2dict))

    # 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
    print(json.dumps(s3, default=lambda obj: obj.__dict__))

