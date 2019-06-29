# author:checky

# 1、格式化类的实例__str__

class Student(object):

    def __init__(self, name):
        self.name = name

    # 格式化实例打印输出的格式
    def __str__(self):
        return "Student object name : " + self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'city':
            return "Student object has no city attr"
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


print(Student("张三"))


# Student object name : 张三

# 2、可迭代的类 __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # def __getitem__(self, item):
    #     a, b = 1, 1
    #     for x in range(item):
    #         a, b = b, a + b
    #     return a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for i in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b

            return L


for i in Fib():
    print(i)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
print(Fib()[5])
# 如果没有定义 __getitem__ 方法，则会发生这个错误
# TypeError: 'Fib' object does not support indexing

# 如果想实现按下标取元素的话，可以用__getitem__方法

f = Fib()
print(f[5])
print(f[6])
print(f[7])


# 如果想Fib类也支持切片的话，需要修改__getitem__ 方法：
def __getitem__(self, n):
    if isinstance(n, int):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for i in range(stop):
            if i >= start:
                L.append(i)
            a, b = b, a + b

        return L


f2 = Fib()
print(f2[3:100])

# __getattr__

# 普通情况下，获取一个实例中没有的属性会报错，但我我们可以通过定义 __getattr__ 来检查是否包含 该属性
s = Student("Grace")
# s.city
# 会直接报错  AttributeError: 'Student' object has no attribute 'city'

# 当在类中加了 __getattr__ 后，就可以友好地打印出获取不到属性的错误了
# s.city1
# AttributeError: 'Student' object has no attribute 'city1'

# __call__ 类的实例可调用
class A(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("Class A __call__ function ")

a = A()
a()
# Class A __call__ function
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
# 把函数看成对象，因为这两者之间本来就没啥根本的区别。
