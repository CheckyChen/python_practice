# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样

# 普通方式，转为 10 进制
print(int('1234'))

# 通过 base 参数，转为 8 进制、 16 进制
print(int('1234', base=8))
print(int('1234', base=16))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))  # 64

# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

max2 = functools.partial(max, 10)
print(max2(1, 4, 3, 6))  # 10
# 实际上会把10作为*args的一部分自动加到左边，也就是


# *********小结**********
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
