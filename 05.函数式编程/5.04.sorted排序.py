# python的默认函数sorted()可以对list排序，默认升序
L = [36, 5, -12, 9, 21]
print(sorted(L))  # [36, 5, -12, 9, 21]

# 绝对值排序
print(sorted(L, key=abs))  # [5, 9, -12, 21, 36]

# 字符串排序
L1 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L1))  # ['Credit', 'Zoo', 'about', 'bob'] 因为 Z < a

# 忽略大小写排序
print(sorted(L1, key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']

# 按照降序排序 reverse = True
print(sorted(L1, key=str.lower, reverse=True))  # ['Zoo', 'Credit', 'bob', 'about']

# 按照名字排序
L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L2, key=lambda t: t[0].lower()))
print(sorted(L2, key=lambda t: t[1]))
