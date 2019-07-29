# author:checky

# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
#
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("消费者：消费-->%s" % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("生产者：生产-->%s" % n)
        r = c.send(n)
        print("生产者：从消费者那里返回-->%s" % r)
    c.close()

c = consumer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#
#   ①首先调用c.send(None)启动生成器；
#
#   ②然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
#   ③consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
#   ④produce拿到consumer处理的结果，继续生产下一条消息；
#
#   ⑤produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

