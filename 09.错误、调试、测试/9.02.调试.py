# author:checky

# 1、普通调试方法
# print()

def foo(s):
    a = int(s)
    print('>> a =', a)
    return 10 / a


# foo('0')


# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。

# 2、断言
# assert

def foo1(s):
    a = int(s)
    assert a != 0, '除数不能为0'
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    # 如果断言失败，assert语句本身就会抛出AssertionError：
    return 10 / a


# foo1('0')
# AssertionError: s 不能为0
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
# 关闭后，你可以把所有的assert语句当成pass来看。
# python -O 9.02调试.py

# 3、将错误日志输出到文件中
# logging

# import logging
#
# logging.basicConfig(level=logging.info())

# s = '0'
# n = int(s)
# logging.info(">> n =", n)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，
# 你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 4、pdb
# 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
s = '0'
n = int(s)
print(10 / n)
# 启用方式：python -m pdb test.py
