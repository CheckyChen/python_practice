# author:checky

# 1、定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(val):
    if val < 0:
        return -val
    else:
        return val


print(my_abs(100))
print(my_abs(-10))


# 2、空函数  函数体用 pass 代替

def none_func():
    pass


# pass 还可以用在其他语句里
def test():
    if False:
        pass


# 3、参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：

# my_abs(1,2)

# TypeError: my_abs() takes 1 positional argument but 2 were given

# my_abs('A')

# TypeError: '<' not supported between instances of 'str' and 'int'


# 完善一下
def my_abs1(val):
    if not isinstance(val, (int, float)):
        raise TypeError("val 只能为整型、浮点型")
    if val > 0:
        return val
    else:
        return -val


# my_abs1("A")

# 4、返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 用一个值来接收返回的多个值
result = move(100, 100, 60, math.pi / 6)
print(result)  # 换回的是一个元组


# 求 a*x*x + b*x + c = 0 的值
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("a只能为数字类型")
    if not isinstance(b, (int, float)):
        raise TypeError("b只能为数字类型")
    if not isinstance(c, (int, float)):
        raise TypeError("c只能为数字类型")

    if int(a) == 0:
        raise ValueError("a的值不能为0")

    if b**2 < 4*a*c:
        raise ValueError("数值错误！b的平方必须大于4ac")

    x1 = -b + math.sqrt(b*b - 4 * a * c) / 2 * a
    x2 = -b - math.sqrt(b*b - 4 * a * c) / 2 * a
    return x1, x2

ret = quadratic(1,1,0)
print(ret)
