# author:checky

class Animal(object):
    pass


# 哺乳动物
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


# 蝙蝠
class Bat(Mammal):
    pass


# 鸵鸟
class Ostrich(Bird):
    pass


# 给动物加上会跑和会飞的功能
class Runnable(object):
    def run(self):
        print("Running...")


class Flyable(object):
    def fly(self):
        print("Flying...")


# 给狗狗加上会跑的功能
class Dog(Mammal, Runnable):
    pass


d = Dog()
d.run()


# Running...

# 给蝙蝠加上会飞的功能
class Bat(Bird, Flyable):
    pass


b = Bat()
b.fly()


# Flying...

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计

class A(object):
    pass
    # def __init__(self):
    #     print("in the A class init")


class B(object):
    def __init__(self):
        print("in the B class init")


class C(A,B):
    pass

c = C()
# 如果C有自己的构造函数，则执行自己的，否则根据 广度优先 原则执行父类的构造函数(__init__())
