# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def calc_sum(*args):
    ret = 0
    for i in args:
        ret = ret + i
    return ret


print(calc_sum(1, 2, 3, 4))


# 求和，返回一个函数
def lazy_sum(*args):
    def sum():
        ret = 0
        for n in args:
            ret = ret + n
        return ret

    return sum


f = lazy_sum(1, 2, 3, 4)
print(f)  # <function lazy_sum.<locals>.sum at 0x000002F10217A2F0>
print(f())  # 10

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1 = lazy_sum(1, 3, 4, 5, 6, 7)
f2 = lazy_sum(1, 3, 4, 5, 6, 7)
# 即使传入相同的参数，返回的函数都不相同
print(f1 == f2)


# 闭包

# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
        print(i)
    return fs


f1, f2, f3 = count()


# f1()
# # 1
# # 2
# # 3
# f2()


# f3()
# print(f1())  # 9
# print(f2())  # 9
# print(f3())  # 9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# ********返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。***********


def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f4, f5, f6 = count1()
print(f4())
print(f5())
print(f6())


# 创建计数器
def createCounter():
    def f(i):
        def g():
            return i + 1

        return g

    fs = []
    i = 0
    # while True:
    #     i = i + 1
    #     fs.append(f(i))
    # return fs


print("------------------------")
print(createCounter()())
print(createCounter()())
print(createCounter()())
print(createCounter()())
