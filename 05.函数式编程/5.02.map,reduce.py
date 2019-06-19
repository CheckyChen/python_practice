# author:checky

# map() 函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 这返回的是一个map对象
print(list(r))

# 将元素转化为字符串
r1 = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r1))

# 2、reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def add(x, y):
    return x + y


r2 = reduce(add, [1, 2, 3, 4, 5])
print(r2)


def fn(x, y):
    return x * 10 + y


r3 = reduce(fn, [1, 2, 3, 4, 5])
print(r3)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


r4 = reduce(fn, map(char2num, '1234567'))
print(r4)

# 整理成一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


L = ['adam', 'LISA', 'barT']


def name_format(name):
    ret = ""
    if name is not None:
        n = 0
        for s in name:
            if n == 0:
                ret = ret + str(s).upper()
            else:
                ret = ret + str(s).lower()
            n = n + 1
    return ret


print(list(map(name_format,L)))
