# author:checky

# 获取对象类型  type()

print(type(123))
# <class 'int'>

print(type("str"))
# <class 'str'>

print(type(None))
# <class 'NoneType'>

print(type(abs))
# <class 'builtin_function_or_method'>

print(type(123) == type(456))
# True
print(type(123) == int)
# True
print(type('abc') == type('123'))
# True
print(type('abc') == str)
# True
print(type('abc') == type(123))
# False

# 判断是否为函数类型
print("===================")
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
# True

print(type(abs) == types.BuiltinFunctionType)
# True

print(type(lambda x: x * x) == types.LambdaType)
# True

print(type((x for x in range(10))) == types.GeneratorType)

# True

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
print("=======")


class Animal(object):
    def __init__(self):
        pass

    def run(self):
        pass


class Dog(Animal):
    pass


# 哈士奇
class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
# True

print(isinstance(h, Dog))
# True

print(isinstance(h, Animal))
# True

print(isinstance(d, Husky))
# False

# **************总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。******


# 使用 dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir("abc"))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',...]

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print(len("abc"))  # 3
print(("abc").__len__())  # 3


class MyDog(object):
    def __len__(self):
        return 100


myDog = MyDog()
print(len(myDog))


# 100

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x ** 2


myobj = MyObject()
print(hasattr(myobj, "x"))
# True

print(hasattr(myobj, "power"))
# True

print(hasattr(myobj, "y"))
# False

setattr(myobj, "y", 9)
print(hasattr(myobj, "y"))
# True

print(getattr(myobj,"y"))
# 9

print(myobj.y)
# 9

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(myobj,"z")
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(myobj,"z",404))
# 404

# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据
