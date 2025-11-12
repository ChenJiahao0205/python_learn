import hashlib

if __name__ == '__main__':
    # Python的hashlib提供了常见的哈希算法，如MD5，SHA1等等
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    md5_2 = hashlib.md5()
    md5_2.update('how to use md5 in '.encode('utf-8'))
    md5_2.update('python hashlib?'.encode('utf-8'))
    print(md5_2.hexdigest())

    # 另一种常见的哈希算法是SHA1
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())