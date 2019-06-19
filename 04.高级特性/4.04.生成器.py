# 不用一次性生成全部列表的元素，而是通过一边循环一边计算后续元素的机制，成为生成器：generator

L = [i * i for i in range(10)]
g = (i * i for i in range(10))
print(g)
print(next(g))
print(next(g))

# 当执行到最后一个元素后，再执行next(g),会报：StopIteration 错误

for i in g:
    print(i)  # 因为前面已经执行了两次，所以这里是从第三个元素 4 开始输出


# 斐波拉切数列
def fib(max):
    a, b, n = 0, 1, 0
    n = 0
    while n < max:
        print(b)
        a, b = b, a + b
        n = n +1
    print("完成")

fib(8)

# 用生成器生成 斐波拉切数列
def fib(max):
    a, b, n = 0, 1, 0
    n = 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n +1
    print("完成")

for i in fib(8):
    print(i)

# 这里比较难理解的就是，generator和函数的执行流程不一样：
# 函数时顺序执行的，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()
# 的时候执行，遇到yield语句返回，再执行时上次返回的yield语句处理执行。












