from base64 import encode
from pyexpat import ParserCreate

from built_in_modules.DefaultSaxHandler import DefaultSaxHandler

if __name__ == '__main__':
    # 操作XML有两种方法：DOM和SAX。
    # DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    # SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
    # 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

    # 例，当SAX解析器读到一个节点时：
    # <a href="/">python</a>
    # 会产生3个事件：
        # start_element事件，在读取<a href="/">时；
        # char_data事件，在读取python时；
        # end_element事件，在读取</a>时。

    # 用代码实验一下
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''

    handler = DefaultSaxHandler()
    parser = ParserCreate()

    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

    # 生成XML 99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append('some & data')
    L.append(r'</root>')
    print(''.join(L))

