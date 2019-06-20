# filter()
# python 内置的函数，用于过滤数列

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 保留奇数
def is_odd(x):
    return x % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # [1, 3, 5, 7, 9]


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["A", "B", None, "  "])))  # ['A', 'B']


# 用filter求素数

# 先从2开始列出所有的自然数，2,3,4,5,6,7,8,9,.....
# 取第一个数 2 它是素数，然后用 2 把所有 2 的倍数的数全去掉，得新数列
# 3,5,7,9,....
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 7, 9, 11,13,17,19,...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7,11, 13, 17, 19, ...
# 不断筛下去，就可以得到所有的素数。

# 构建一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for i in primes():
    if i < 100:
        print(i)
