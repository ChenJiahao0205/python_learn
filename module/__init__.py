from module.hello import test

if __name__ == '__main__':

    test()


    # ===================================================作用域===================================================
    # 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

    # private函数或变量不应该被别人引用
    def _private_1(name):
        return 'Hello, %s' % name

    def _private_2(name):
        return 'Hi, %s' % name

    def greeting(name):
        if len(name) > 3:
            return _private_1(name)
        else:
            return _private_2(name)