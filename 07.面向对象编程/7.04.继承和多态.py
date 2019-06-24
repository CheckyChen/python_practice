# author:checky

# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。

class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    def eat(self):
        print("dog is eating")


class Cat(Animal):
    pass

# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。

dog = Dog()
dog.run()  # animal is running ，自动继承了父类的方法
dog.eat()  # dog is eating ，自定义的方法

cat = Cat()
cat.run()


# 重写父类的方法

class Dog(Animal):
    def run(self):
        print("dog is running")


class Cat(Animal):
    def run(self):
        print("cat is running")


dog1 = Dog()
dog1.run()  # dog is running

cat1 = Cat()
cat1.run()  # cat is running

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。

# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。

print(isinstance(dog1, Dog))  # True
print(isinstance(dog1, Animal))  # True

animal = Animal()
print(isinstance(animal, Dog))  # False

# 狗一定是动物，但是动物反过来，不一定是都是狗

# 多态：
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
# animal is running
# animal is running

run_twice(Dog())
# dog is running
# dog is running

run_twice(Cat())
# cat is running
# cat is running

class Tortoise(Animal):
    def run(self):
        print("tortoise is running slowly...")

run_twice(Tortoise())
# tortoise is running slowly...
# tortoise is running slowly...

# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，
# 然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
# 就会自动调用实际类型的run()方法，这就是多态的意思：
#
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
# 这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，
# 不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 静态语言 和 动态语言 对比

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print("start...")

run_twice(Timer())
# start...
# start...

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
