# author:checky

# 1、定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(val):
    if val<0:
        return -val
    else:
        return val

print(my_abs(100))
print(my_abs(-10))

# 2 空函数  函数体用 pass 代替

def none_func():
    pass

# pass 还可以用在其他语句里
def test():
    if False:
        pass