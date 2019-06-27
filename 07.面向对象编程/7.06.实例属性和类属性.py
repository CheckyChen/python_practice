# author:checky

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    # 类属性
    school = "HuST University"

    def __init__(self, name):
        # 实例属性
        self.name = name


s = Student("Checky")
s.Score = 90  # score 实例属性

print(Student.school)
# HuST University

# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
s1 = Student("Bob")
print(s1.name, s1.school)


# HuST University

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

class Count(object):
    count = 0

    def __init__(self):
        Count.count = Count.count + 1


c1 = Count()
print(c1.count)
# 1
c2 = Count()
print(c2.count)
# 2
c3 = Count()
print(c3.count)
# 3
c4 = Count()
print(c4.count)
# 4
