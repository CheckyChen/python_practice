# author:checky

# 1、错误处理
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

# try
def except_test(a, b):
    try:
        print("trying")
        r = a / int(b)
        print("result=", r)
    except ValueError as e:
        print("except:", e)
    except ZeroDivisionError as e:
        print("except:", e)
    else:
        print("no errors")
    finally:
        print("finally...")
    print("end")


except_test(10, 0)
# trying
# except: division by zero
# finally...
# end

except_test(10, 2)
# trying
# result= 5.0
# no errors
# finally...
# end

except_test(10, 'a')
# trying
# except: invalid literal for int() with base 10: 'a'
# finally...
# end


# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，
# 它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

try:
    pass
except ValueError as e:
    pass
except UnicodeError as e:
    pass


# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：

def foo(s):
    return 10 / int(s)


def bar(a):
    return foo(a) * 2


def main():
    try:
        bar(0)
    except BaseException as e:
        print("except:", e)


main()


# except: division by zero
# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。

# 2、记录错误日志
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#
# Python内置的logging模块可以非常容易地记录错误信息：

# import logging
# def except_test1():
#     try:
#         a = 10 / 0
#     except BaseException as e:
#         logging.exception(e)
#     finally:
#         print("finally...")
#
#
# except_test1()


# 3、自定义异常类
class MyException(BaseException):
    pass


def test(a):
    if a == 0:
        raise MyException("发生了错误了...")


# test(0)  # 会报错的


# ********尽量使用Python内置的错误类型************

# 层层网上抛异常

def f1(n):
    v = int(n)
    if v == 0:
        raise ValueError("被除数不能为0")
    return 10 / v


def f2():
    try:
        f1(0)
    except ValueError as e:
        print("ValueError...")
        raise  # raise语句如果不带参数，就会把当前错误原样抛出


f2()
# ValueError: 被除数不能为0
