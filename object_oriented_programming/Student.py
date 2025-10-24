class Student(object):
    # 类属性
    name = 'Student'

    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
    def __init__(self, name, score, age):
        # 实例属性
        self.name = name
        self.score = score
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__age = age

    # 数据封装
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    # 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age