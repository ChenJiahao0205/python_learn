from types import MethodType

from object_oriented_advanced_programming.Student import Student
from object_oriented_advanced_programming.Student2 import Student2

if __name__ == '__main__':
    # 面向对象高级编程

    s = Student()
    # 动态给实例绑定一个属性
    s.name = 'cjh'
    print(s.name)

    # 定义一个函数作为实例方法
    def set_age(self, age):
        self.age = age

    # 给实例动态绑定一个方法
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)

    # 上述写法 给一个实例绑定的方法，对另一个实例是不起作用的
    s2 = Student()  # 创建新的实例
    # s2.set_age(25)  # 尝试调用方法
    # print(s2.age)  # 报错

    # 给所有实例都绑定方法，可以给class绑定方法
    def set_score(self, score):
        self.score = score

    # 给class绑定方法
    Student.set_score = set_score

    # 给class绑定方法后，所有实例均可调用
    s.set_score(100)
    print(s.score)
    s2.set_score(99)
    print(s2.score)

    # 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

    # 使用__slots__ 限制实例的属性
    # 只允许对Student实例添加name、age、score、set_age(这是一个实例方法，也会受到限制)
    # Student中定义了__slots__


    # 使用@property

    # 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
    s.score = 9999
    print(s.score)

    # 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
    s3 = Student()
    # ok!
    s3.set_year(60)
    print(s3.get_year())

    # 报错 raise ValueError('score must between 0 ~ 100!')
    s3.set_year(999)
    print(s3.get_year())


    # @property 负责把一个方法变成属性调用的
    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@year.setter，负责把一个setter方法变成属性赋值
    s4 = Student2()
    # # OK，实际转化为s.score(60)
    s4.year = 60
    # OK，实际转化为s.score()
    print(s4.year)

    # 多重继承
    # 通过多重继承，一个子类就可以同时获得多个父类的所有功能