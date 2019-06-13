# 1、列表  list

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

list1 = ["Tom", "France", "Jack", "Jay"]
print(list1)

# 1.1 获取列表的长度
print(len(list1))

# 1.2 取其中的一个值
print(list1[0])

# 取最后一个值
print(list1[-1])

# 1.3 往列表里添加一个元素
list1.append('Checky')
print(list1)

# 1.4 把元素插入到指定位置
list1.insert(1, 'Tony')
print(list1)

# 1.5 删除末尾的元素
el = list1.pop()
print(el, list1)

# 删除指定位置的元素
print(list1)
list1.pop(1)  # i 为列表的索引值
print(list1)

# 1.6 替换指定位置的值
print(list1)
list1[1] = 'Gray'
print(list1)

# 列表里面的数据类型也可以不一致
list2 = ['字符串', 1, False, 2.444]
print(list2)

# 列表也可以包含另外一個列表，二维列表
list3 = [1, 'string', ['string', 1, True, None], 2.55]
print(list3, len(list3))  # 长度为 4 ，因为 ['string', 1, True, None] 只能算是其中一个元素
# 想要拿到 二维列表中的值
print(list3[2][2])

# 2、元组 tuple

# tuple和list非常类似，但是tuple一旦初始化就不能修改
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
t1 = ('France', "Gray", 'Checky', 'Jay')
print(t1)

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t2 = (1, 2)

# 定义一个空元组
t3 = ()

# 定义只有一个元素的元组,必须得有逗号
# 这是因为括号()既可以表示tuple，又可以表示【数学公式中的小括号】，这就产生了歧义
t4 = ('france',)
t5 = ('france') # 这个就只能表示为 字符串 'france' 了
print(t4, t5)

# "可变元组"
t6 = ("Jack","France",["Gray","Jay"])
print(t6)
t6[2][0] = "Checky"
print(t6)
