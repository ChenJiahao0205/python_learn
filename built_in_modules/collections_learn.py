import argparse
import os
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

if __name__ == '__main__':
    # collections是Python内建的一个集合模块，提供了许多有用的集合类。

    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)

    # 如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
    # namedtuple('名称', [属性list]):
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(1, 2, 3)
    print(c.x)
    print(c.y)
    print(c.r)

    # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)

    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    # # key2不存在，返回默认值
    print(dd['key2'])

    # 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序 如果要保持Key的顺序，可以用OrderedDict
    # # dict的Key是无序的
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)

    # od # OrderedDict的Key是有序的(OrderedDict的Key会按照插入的顺序排列，不是Key本身排序)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)

    # ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找
    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = { k: v for k, v in vars(namespace).items() if v }

    # 组合成ChainMap:
    combined = ChainMap(command_line_args, os.environ, defaults)

    # 打印参数:
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])

    # Counter是一个简单的计数器，例如，统计字符出现的个数
    c = Counter('programming')
    for ch in 'programming':
        c[ch] = c[ch] + 1

    print(c)



