# author:checky

def now():
    print('2019年6月20日22:41:57')


f = now
print(f.__name__)  # 可以得到函数的名称


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kwargs):
        print("调用了 %s()" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


# 借助Python的@语法，把decorator置于函数的定义处：
@log
def now1():
    print('2019年6月20日22:51:46')


now1()


# 调用了 now1()
# 2019年6月20日22:51:46

# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("log text is %s,func %s()" % (str(text), func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log("excute")
def now2():
    print("2019年6月21日07:01:54")


now2()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now3 = log('execute')(now2)
# 首先执行log('execute'),，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print(now3.__name__)

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
# 所以，一个完整的decorator的写法如下：
import functools


def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("func name is %s" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


# 带参数的装饰器
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("func name : %s , log text : %s " % (func.__name__, text))
            return func

        return wrapper

    return decorator


@log2("日志文本")
def now4():
    print("2019年6月21日07:14:26")


now4()

# 打印函数运行的时间
import time
import datetime


def calc_time(text):
    t1 = datetime.datetime.now()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s(),运行中..." % func.__name__)
            return func

        return wrapper

    t2 = datetime.datetime.now()
    print("%s()运行时间为:%s" % ("", (t2 - t1).seconds))

    return decorator


@calc_time("a")
def func():
    time.sleep(10)


func()
