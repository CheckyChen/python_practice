# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 求一个列表内的每个元素的平方

# 1、传统做法
L = []
for i in list(range(0, 11)):
    L.append(i * i)
print(L)

# 2、新方法，一句话就够了
print([i * i for i in list(range(0, 11))])

# 取出所有偶数的平方
print([i * i for i in list(range(0, 11)) if i % 2 == 0])

# 取出3的倍数
l1 = [i for i in list(range(0, 11)) if i % 3 == 0]
print(l1)

# 3、使用两层循环，生成全排列
l2 = [i + j for i in 'ABC' for j in 'XYZ']
print(l2)

# 4、循环字典
d1 = {'a': 'X', 'b': 'Y', 'c': 'Z'}
l3 = [k + '=' + v for k, v in d1.items()]
print(l3)

# 5、处理列表数据
l4 = ["Apple", "Banana", "Orange"]
l5 = [i.lower() for i in l4]
print(l5)
