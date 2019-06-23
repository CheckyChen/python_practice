# author:checky

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
#
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、age属性：

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
# 就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，把Student类改一改：

class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_age(self):
        print("%s : %s" % (self.__name, self.__age))

    def print_name(self):
        print("%s" % self.__name)

    # 在方法中，可以对参数做检查，避免传入无效的参数：
    def set_age(self, age):
        if isinstance(age,int)==True:
            self.__age = age
        else:
            raise ValueError("年龄必须整数")


stu = Student("checky", 27)
# print(stu.__name)
# AttributeError: 'Student' object has no attribute '__name'
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

stu.print_age()  # checky : 27 # 这个是通过内部的实现获取的名字和年龄  不会报错

# 如果想修改私有变量age怎么办，可以在类中添加一个方法：set_age

stu.set_age(28)
stu.print_age()  # checky : 28

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

print(stu._Student__name)  # checky

# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
#
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# 特别注意下面呢这种写法：

stu.print_name()

stu.__name = "checky2"
print(stu.__name)  # checky2
# 表面上看起来属性 __name 是被修改了，但是实际上是没改的，只是添加了个新的 __name 属性而已
# 内部的__name变量已经被Python解释器自动改成了_Student__name

# 重新获取 stu 内部的name属性
stu.print_name() # checky ,任然打印的是 checky

# stu.set_age("111") # ValueError: 年龄必须整数
stu.set_age(25)
stu.print_age()