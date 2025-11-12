import sys

if __name__ == '__main__':
    # 在命令行程序中，经常需要获取命令行参数。Python内置的sys.argv保存了完整的参数列表，我们可以从中解析出需要的参数
    print(sys.argv)
    source = sys.argv[1]
    target = sys.argv[2]

    # 使用argparse解析参数，只需定义好参数类型，就可以获得有效的参数输入，能大大简化获取命令行参数的工作。