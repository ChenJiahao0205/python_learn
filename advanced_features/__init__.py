def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles(n):
    L = []
    for o in range(n):
        L2 = []
        for i in range(o + 1):
            if i == 0 or i == o:
                L2.append(1)
            else:
                L2.append(L[i] + L[i - 1])
        L = L2
        yield L2

if __name__ == '__main__':
    # =============================切片=============================
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[0])
    print(L[1])
    print(L[-1])

    # 取前n个元素
    r = []
    n = 3
    for i in range(n):
        r.append(L[i])
    print(r)

    # =============================切片操作=============================
    print(L[0:4])

    # =============================第一个索引是0时 可以省略================
    print(L[:3])
    print(L[1:3])
    print(L[-2:])

    L = list(range(100))
    # =============================取前10个数=============================
    print(L[:10])
    # =============================取后10个数=============================
    print(L[-10:])

    # =============================取11~20个数=============================
    print(L[10:20])

    # =============================前10个数，每两个取一个=============================
    print(L[:10:2])
    # =============================所有数，每5个取一个===============================
    print(L[::5])
    # =============================原样复制一个list===============================
    print(L[:])

    # tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
    A = (0, 1, 2, 3, 4, 5)
    print(A[:3])

    # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
    str = 'ABCDEFG'
    print(str[:3])
    print(str[::2])



    # =============================迭代===============================
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key)

    for value in d.values():
        print(value)

    for ch in 'ABC':
        print(ch)

    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)

    # =============================列表生成式===============================
    # 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
    print(list(range(1, 11)))

    # 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]  方法一是循环：
    L = []
    for x in range(1, 11):
        L.append(x * x)
    print(L)

    # 列表生成式则可以用一行语句代替循环生成上面的list
    L2 = [x * x for x in range(1, 11)]
    print(L2)

    L3 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(L3)

    L4 = [m + n for m in 'ABC' for n in 'XYZ']
    print(L4)

    # for循环其实可以同时使用两个甚至多个变量
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    for k, v in d.items():
        print(k, '=', v)

    L = ['Hello', 'World', 'IBM', 'Apple']
    print(L)
    print([s.lower() for s in L])

    # for循环后只能放if  for循环前 可以放if和else
    L = [x if x % 2 == 0 else -x for x in range(1, 11)]
    print(L)

    # =============================生成器===============================
    # 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素
    L = [x * x for x in range(10)]
    print(L)
    # g并不是一次生成的
    g = (x * x for x in range(10))
    print(g)

    # 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
    # 可以通过next()函数获得generator的下一个返回值
    for n in g:
        print(n)

    print(fib(5))

    # fib函数和generator仅一步之遥。要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：

    g2 = fib2(5)
    for n in g2:
        print(n)

    # 杨辉三角
    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

    for t in triangles(6):
        print(t)

