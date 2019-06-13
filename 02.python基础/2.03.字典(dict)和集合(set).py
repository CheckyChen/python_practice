# author:checky

# 1、字典 dict

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

# 1.1 声明
scores = {"France": 85, "Checky": 100, "Gray": 150}
print(scores)

d1 = {'apple': 3.6, 'banana': 2}
print(d1)

# 1.2 取值
print(d1['apple'])
# print(d1['orange'])  # 因为d1中不存在 key 为 orange 的字典，所以会报错
print(d1.get('orange',None)) # 这种方式可以避免程序报错，如果不存在 orange ，则会返回 None

# 1.3 删除一个 key 和 value ：pop(key)

d2 = {"a":140000,"b":12000,"c":"string"}
print(d2)
d2.pop("b")
print(d2)

##############dict的key必须是不可变对象，比如字符串和整数都是不可变的，可以作为key，但是list是可变的，不可作为key#############

# 2、集合 set

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3,4,4,6])
print(s) # 重复的 key 4 会被自动去重掉

# 2.1 添加元素  add(value)

s.add(7)
print(s)

# 2.2 删除元素 remove(value)

s.remove(2)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1&s2) # 交集
print(s1|s2) # 并集

# 小结
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。
#
# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。

