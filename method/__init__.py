import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 有了power2(x, n)时 power(x) 会被覆盖报错 需要改为power(x, n = 2)
# def power(x):
#     return x * x
def power(x, n = 2):
    return x * x

def power2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=[]):
    L.append('END')
    return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person3(name, age, *, city, job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


if __name__ == '__main__':
    r1 = 12.34
    r2 = 9.08
    r3 = 73.1
    s1 = 3.14 * r1 * r1
    s2 = 3.14 * r2 * r2
    s3 = 3.14 * r3 * r3
    print(s1)
    print(s2)
    print(s3)

    print(abs(100))
    print(abs(-20))
    print(max(2, 3, 1, -5))

    # ===============================类型转换===============================
    print(int('123'))
    print(int(12.34))
    print(str(100))
    print(str(1.23))
    print(float('12.34'))
    print(bool(1))
    print(bool(0))

    a = 100
    b = a
    print(a)
    print(b)

    a = 90
    print(a)
    print(b)

    # ==================函数必须被定义在调用前!!!==================
    print(my_abs(-99))

    # ==================函数返回多个结果!!!==================
    x, y = move(100, 100, 60, math.pi / 6)
    print(x)
    print(y)

    # =======================函数的参数=======================
    print(power(5))
    print(power(15))

    print(power(5, 2))
    print(power(5, 3))

    print(add_end([1, 2, 3]))
    print(add_end(['x', 'y', 'z']))

    # ['END']
    print(add_end())
    # ['END', 'END'] 定义默认参数要牢记一点：默认参数必须指向不变对象！
    print(add_end())

    print(calc([1, 2, 3]))
    print(calc((1, 3, 5, 7)))
    print(calc2(1, 2, 3))
    print(calc2(1, 3, 5, 7))
    print(calc2(1, 2))
    print(calc2())

    nums = [1, 2, 3]
    print(calc2(*nums))

    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')

    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)

    person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

    # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    person3('Jack', 24, city='Beijing', job='Engineer')

    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x=99)
    f2(1, 2, d=99, ext=None)

    # 递归函数
    print(fact(1))
    print(fact(5))
    print(fact(100))
    # = > fact(5)
    # = > 5 * fact(4)
    # = > 5 * (4 * fact(3))
    # = > 5 * (4 * (3 * fact(2)))
    # = > 5 * (4 * (3 * (2 * fact(1))))
    # = > 5 * (4 * (3 * (2 * 1)))
    # = > 5 * (4 * (3 * 2))
    # = > 5 * (4 * 6)
    # = > 5 * 24
    # = > 120

    print(fact2(5))
    # = > fact_iter(5, 1)
    # = > fact_iter(4, 5)
    # = > fact_iter(3, 20)
    # = > fact_iter(2, 60)
    # = > fact_iter(1, 120)
    # = > 120


