# author:checky

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):
    pass


s = Student()
s.name = "checky"
s.age = 27
s.gender = "男"
print(s.name, s.age, s.gender)


# checky 27 男

# 还可以给实例绑定一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # # 给实例绑定一个方法
s.set_age(28)
print(s.age)
# 28

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s1 = Student()


# s1.set_age(26)
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s1.set_score(100)
print(s1.score)
# 100

s2 = Student()
s2.set_score(150)
print(s2.score)


# 150


# 使用__slots__

# 为了限制给类乱添加属性或方法，定义了一个 __slots__ 变量来限制class实例能添加的属性
class Teacher(object):
    __slots__ = ("name", "age", "hobby")

    def __init__(self, name, age):
        self.name = name
        self.age = age


t = Teacher("France", 30)
print(t.name, t.age)
# t.gender = "男"
# AttributeError: 'Teacher' object has no attribute 'gender'
t.hobby = "Basketball"
print(t.name, t.age, t.hobby)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class PETeacher(Teacher):
    pass


pt = PETeacher("Grace", 35)
pt.gender = "男"  # 这个不会报错，因为父类的__slots__ 对子类不起作用
print(pt.name, pt.age, pt.gender)


# Grace 35 男

class MusicTeacher(Teacher):
    __slots__ = ("city",)
    pass


mt = MusicTeacher("Selina", 29)
# mt.gender = "女"
# AttributeError: 'MusicTeacher' object has no attribute 'gender'
mt.hobby = "Dance"
mt.city = "BeiJing"
print(mt.name, mt.age, mt.hobby, mt.city)
# Selina 29 Dance BeiJing

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
