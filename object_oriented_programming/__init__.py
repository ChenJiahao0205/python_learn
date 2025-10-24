import types

from object_oriented_programming.Animal import Animal
from object_oriented_programming.Cat import Cat
from object_oriented_programming.Dog import Dog
from object_oriented_programming.Student import Student

if __name__ == '__main__':
    # =======================================面向对象编程=======================================

    # 类和实例
    # cjh = Student()
    # print(cjh)

    # cjh.name = 'chen'
    # print(cjh.name)

    cjh = Student('cjh', 99, 18)
    print(cjh)
    print(cjh.name)
    print(cjh.score)

    cjh.print_score()

    print(cjh.get_grade())

    # 报错 私有的 外部无法访问
    # cjh.age

    # 通过方法封装私有属性可以访问
    print(cjh.get_age())

    print(cjh.set_age(28))

    print(cjh.get_age())

    # 打破私有（不推荐）
    print(cjh._Student__age)

    # 继承
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()

    # a是list类型
    a = list()
    # b是Animal类型
    b = Animal()
    # c是Dog类型
    c = Dog()

    # 判断一个变量是否是某个类型可以用isinstance()
    print(isinstance(a, list))
    print(isinstance(b, Animal))
    print(isinstance(c, Dog))

    print(isinstance(c, Animal))

    def run_twice(animal):
        animal.run()
        animal.run()


    run_twice(Animal())
    run_twice(Dog())

    # 获取对象信息
    # 判断对象类型
    # 基本类型都可以用type()判断
    print(type(123))

    # 变量指向函数或者类，也可以用type()判断
    print(type(abs))
    print(type(a))

    print(type(123)==type(456))
    print(type(123)==int)
    print(type('abc')==type('123'))
    print(type('abc')==str)
    print(type('abc')==type(123))

    # 判断一个对象是否是函数
    # 使用types模块中定义的常量
    def fn():
        pass

    print(type(fn)==types.FunctionType)
    print(type(abs)==types.BuiltinFunctionType)
    print(type(lambda x: x)==types.LambdaType)
    print(type((x for x in range(10)))==types.GeneratorType)

    # 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

    # 使用dir()
    # 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
    print(dir('ABC'))
