# author:checky

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）

d = {'a': 1, 'b': 2, 'c': 3}

# 默认迭代的是d的key
for key in d:
    print(key, d[key])

# 迭代d的values
for value in d.values():
    print(value)

# 迭代d的key和value
for k, v in d.items():
    print(k, v)

# 通过collections模块的Iterable类型判断对象是否为可迭代对象
from collections import Iterable

print(isinstance('abc', Iterable))
# True
print(isinstance([1, 2, 3, 4], Iterable))
# True
print(isinstance(123, Iterable))
# False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, v in enumerate(['a', 'b', 'c', 'd']):
    print(i, v)

print('==========')
# for 循环里同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

l = [1, 2, 3, 4, 5, 6, 0, 88, 100, 22]


def get_max_min(list):
    '''获取列表的最大值和最小值'''
    max, min = 0, 0
    if len(list) == 0:
        return (None, None)
    else:
        for i in list:
            if i <= min:
                min = i
            if i >= max:
                max = i
        return (max, min)

print(get_max_min(l))
print(get_max_min([]))
