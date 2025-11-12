from datetime import datetime, timedelta

if __name__ == '__main__':
    # datetime是Python处理日期和时间的标准库。
    # 获取当前datetime
    now = datetime.now()
    print(now)
    print(type(now))

    # 获取指定日期和时间
    dt = datetime(2015, 4, 19, 12, 20, 15)
    print(dt)

    # datetime转换为timestamp
    print(dt.timestamp())

    # timestamp转换为datetime
    t = 1429417215.0
    print(datetime.fromtimestamp(t))

    # timestamp也可以直接被转换到UTC标准时区的时间
    # 本地时间
    print(datetime.fromtimestamp(t))
    # UTC时间
    print(datetime.utcfromtimestamp(t))

    # str转换为datetime
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

    # datetime转换为str
    print(now.strftime('%a, %b %d %H:%M'))

    # datetime加减
    # 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
    now2 = datetime.now()
    print(now2 + timedelta(hours=10))

    print(now2 - timedelta(days=1))

    print(now2 + timedelta(days=2, hours=12))