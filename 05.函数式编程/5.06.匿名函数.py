# author:checky

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便

# 是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))  # [1, 4, 9, 16, 25, 36]

f = lambda x: x * x
print(f(10))  # 100

f1 = lambda x: x + 1
print(f1) # <function <lambda> at 0x000002C8359E8EA0>
