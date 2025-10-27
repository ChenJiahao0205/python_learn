class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    # 定义 __repr__ 这里是简化了写法
    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

        if attr == 'age':
            return lambda: 25

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s.' % self.name)