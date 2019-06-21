import sys

'''
测试模块
'''
def test():
    args = sys.argv  # 用list存储了命令行的所有参数
    # argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    # 运行python3 hello.py获得的sys.argv就是['hello.py']
    # 运行python3 hello.py abc获得的sys.argv就是['hello.py', 'abc']。
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello,%s!" % args[1])
    else:
        print("too many arguments")


def __private():
    print("这是个私人方法")


__privateVar = 1000


if __name__ == "__main__":
    test()
