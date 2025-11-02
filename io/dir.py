import os
import shutil

if __name__ == '__main__':
    # 系统类型
    # 如果是posix，说明系统是Linux、Unix或macOS，如果是nt，就是Windows系统
    print(os.name)

    # 环境变量
    print(os.environ)

    # 要获取某个环境变量的值，可以调用os.environ.get('key')
    print(os.environ.get('APPDATA'))

    # 操作文件和目录
    # 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用

    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))

    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
    print(os.path.join('D:/PyCharm/WorkSpace/python_learn/io', 'testdir'))

    # 然后创建一个目录
    # os.mkdir('D:/PyCharm/WorkSpace/python_learn/io/testdir')

    # 删掉一个目录
    # os.rmdir('D:/PyCharm/WorkSpace/python_learn/io/testdir')

    # 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
    # ('D:/PyCharm/WorkSpace/python_learn/io', 'testdir')
    print(os.path.split('D:/PyCharm/WorkSpace/python_learn/io/testdir'))

    # os.path.splitext()可以直接让你得到文件扩展名
    print(os.path.splitext('D:/PyCharm/WorkSpace/python_learn/io/testdir'))

    # 对文件重命名
    # os.rename('D:/PyCharm/WorkSpace/python_learn/io/test.txt', 'D:/PyCharm/WorkSpace/python_learn/io/test.py')

    # 删掉文件
    # os.remove('D:/PyCharm/WorkSpace/python_learn/io/test.py')

    # 复制文件
    shutil.copyfile('D:/PyCharm/WorkSpace/python_learn/io/test.txt', 'D:/PyCharm/WorkSpace/python_learn/io/test1.txt')

    print('========================================================')
    # 过滤文件。比如我们要列出当前目录下的所有目录
    print([x for x in os.listdir('.') if os.path.isdir(x)])

    # 列出所有的.py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])