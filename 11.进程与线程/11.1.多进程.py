# author:checky

# 1.multiprocessing
# multiprocessing模块提供了一个Process类来代表一个进程对象

from multiprocessing import Process
import os


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

def test_proc():
    print("Parent process %s." % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")
    p.start()
    p.join()
    print("Child process end")


# 2.Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
import time, random
from multiprocessing import Pool


def long_time_task(name):
    print("run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("task %s runs %0.2f seconds." % (name, end - start))


def test_proc1():
    print("parent process %s." % os.getpid())
    p = Pool(4)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print("等待所有子进程完成...")
    p.close()
    p.join()
    print("所有子进程完成。")


# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# 3.进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

def write(q):
    print("Process to write:%s" % os.getpid())
    for i in ["A", "B", "C"]:
        print("put element（%s） to Queue..." % i)
        q.put(i)
        time.sleep(random.random())


def read(q):
    print("Process to read:%s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


from multiprocessing import Queue
def test_read_write():
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()




if __name__ == "__main__":
    # test_proc()
    # test_proc1()
    test_read_write()
