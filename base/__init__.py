# 数据类型和变量
if __name__ == '__main__':

    # =============================变量=============================
    a = 5
    a1 = 'a1'
    f = 3.1415

    print('I\'m \"OK\"!')

    print('''line1
    ... line2
    ... line3''')

    # =============================字符串的不可变性=============================

    a3 = 'abc'
    b3 = a3.replace('a', 'A')
    print(a3)
    print(b3)



    # =============================list、tuple=============================

    classmates = ['Michael', 'Bob', 'Tracy']
    classmates.insert(1, '2')
    classmates.append('1')
    print(classmates)
    print(classmates[-1])

    t1 = (1)
    t2 = (1,)

    print(t1)
    print(t2)

    # =============================条件判断=============================

    if 2 > 1:
        print('true')

    print('2')

    birth = int(input('birth: '))
    if birth < 2000:
        print('00前')
    else:
        print('00后')

    # birth = input('birth: ')
    # if birth < 2000:
    #     print('00前')
    # else:
    #     print('00后')


    # =============================模式匹配=============================

    score = 'B'

    match score:
        case 'A':
            print('score is A.')
        case 'B':
            print('score is B.')
        case 'C':
            print('score is C.')
        case _:  # _表示匹配到其他任何情况
            print('score is ???.')

    score = int(input('score:'))

    match score:
        case s if s > 1:
            print('score is A.')
        case s if s > 2:
            print('score is B.')
        case s if s > 3:
            print('score is C.')
        case _:  # _表示匹配到其他任何情况
            print('score is ???.')

    age2 = 15

    match age2:
        case x if x < 10:
            print(f'< 10 years old: {x}')
        case 10:
            print('10 years old.')
        case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
            print('11~18 years old.')
        case 19:
            print('19 years old.')
        case _:
            print('not sure.')


    # =============================循环=============================
    names = ['Michael', 'Bob', 'Tracy']

    for name in names:
        print(name)

    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum + x
    print(sum)

    print(list(range(5)))

    sum2 = 0
    for x in range(101):
        sum2 = sum2 + x
    print(sum2)

    sum3 = 0
    n = 99
    while n > 0:
        sum3 = sum3 + n
        n = n - 2
    print(sum3)

    n = 1
    while n <= 100:
        if n > 10:  # 当n = 11时，条件满足，执行break语句
            break  # break语句会结束当前循环
        print(n)
        n = n + 1
    print('END')

    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0:  # 如果n是偶数，执行continue语句
            continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
        print(n)

    # =============================字典=============================
    d2 = {}
    d2['Adam'] = 67
    print(d2['Adam'])

    if 'Adam' in d2:
        print('存在Adam')

    print(d2.get('Adam'))
    print(d2.get('Adam1'))
    print(d2.get('Adam1', 'REF_DEFAULT'))

    d2['Adam1'] = 68
    print(d2.get('Adam1'))
    d2.pop('Adam1')
    print(d2.get('Adam1'))
    print(d2.get('Adam1', 'REF_DEFAULT'))

    s = {1, 2, 3}
    print(s)
    s.add(4)
    print(s)
    s.add(5)
    print(s)
    s.remove(2)
    print(s)

    s2 = {1, 2, 3}
    s3 = {2, 3, 4}
    print(s2 & s3)
    print(s2 | s3)


