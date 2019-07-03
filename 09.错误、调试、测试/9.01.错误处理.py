# author:checky

# 1、错误处理
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

# try
def except_test(a, b):
    try:
        print("trying")
        r = a / b
        print("result=", r)
    except ZeroDivisionError as e:
        print("except:", e)
    finally:
        print("finally...")
    print("end")


except_test(10, 0)
# trying
# except: division by zero
# finally...
# end

except_test(10,2)
# trying
# result= 5.0
# finally...
# end



# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，
# 而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
