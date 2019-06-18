# author:checky

# 取一个list或tuple的部分元素是非常常见的操作

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前三个
l1 = L[0:3]
l2 = L[:3]
print(l1)
print(l2)

# 取第二个到第三个
l3 = L[1:3]
print(l3)

# 取倒数第一个
l4 = L[-1]
print(l4)

# 取倒数第第二个到倒数第一个
l5 = L[-2:]
print(l5)

l6 = L[-2:1] # 空列表
print(l6)

# 创建一个0到99的列表
L2 = list(range(100))
print(L2)

# 取后十个
l7 = L2[-10:]
print(l7)

# 取前十个，每两个取一个
l8 = L2[:10:2]
print(l8)

# 取所有的，每5个取一个
l9 = L2[::5]
print(l9)

# 复制一个列表
l10 = L2[:]
print(l10)

# 字符串也可以切片
str1 = 'abcdefghijklmnopqrst'
print(str1[:10])
print(str1[-2:])

# 元组也可以切片
t1 = ('a','b','c','d','e')
print(t1[:3])