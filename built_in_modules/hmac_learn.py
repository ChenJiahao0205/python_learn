import hmac

if __name__ == '__main__':
    # Python自带的hmac模块实现了标准的Hmac算法
    message = b'Hello, world!'
    key = b'secret'
    h = hmac.new(key, message, digestmod='MD5')
    print(h.hexdigest())