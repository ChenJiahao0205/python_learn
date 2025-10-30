import logging

if __name__ == '__main__':
    # 错误处理
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')

    print('=================================================')

    try:
        print('try...')
        r = 10 / int('a')
        print('result:', r)
    # 多个except来捕获不同类型的错误
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    finally:
        print('finally...')
    print('END')

    print('=================================================')

    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    # 当没有错误发生时，会自动执行else语句
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

    print('=================================================')

    # 记录错误
    # Python内置的logging模块可以非常容易地记录错误信息
    try:
        # 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
        10 / int('a')
    except Exception as e:
        print("aaa")
        logging.exception(e)
    print('do some')

    # 抛出错误
    # raise
    class FooError(ValueError):
        pass

    def foo(s):
        n = int(s)
        if n == 0:
            raise FooError('invalid value: %s' % s)
        return 10 / n

    foo('0')


    print('===============================================')

    def foo(s):
        n = int(s)
        if n == 0:
            raise ValueError('invalid value: %s' % s)
        return 10 / n


    def bar():
        try:
            foo('0')
        except ValueError as e:
            print('ValueError!')
            # 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了
            # 捕获错误目的只是记录一下，便于后续追踪
            raise

    bar()