# author:checky
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
#
# 用asyncio实现Hello world代码如下：

import asyncio


@asyncio.coroutine
def hello():
    print("hello world!!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("hello again!!")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
#
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
#
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

import threading


@asyncio.coroutine
def hello1():
    print("hello world!! (%s)" % threading.current_thread())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("hello again!!(%s)" % threading.current_thread())


# loop1 = asyncio.get_event_loop()
# task = [hello1(), hello1()]
# loop1.run_until_complete(asyncio.wait(task))
# loop1.close()

# hello world!! (<_MainThread(MainThread, started 13924)>)
# hello world!! (<_MainThread(MainThread, started 13924)>)
# hello again!!(<_MainThread(MainThread, started 13924)>)
# hello again!!(<_MainThread(MainThread, started 13924)>)

# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 可见3个连接由一个线程通过coroutine并发完成。

# 小结
# asyncio提供了完善的异步IO支持；
# 异步操作需要在coroutine中通过yield from完成；
# 多个coroutine可以封装成一组Task然后并发执行。
