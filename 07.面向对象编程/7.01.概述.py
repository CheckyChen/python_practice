# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
#
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
#
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
#
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
#
# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
#
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

std1 = {"name": "张三", "score": 99}
std2 = {"name": "李四", "score": 100}


def print_score(student):
    print("%s,%d" % (student["name"], student["score"]))


print_score(std1)
print_score(std2)


# 如果用类实现的话

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score_cls(self):
        print("%s,%d" % (self.name, self.score))


std3 = Student("王五", 100)
std4 = Student("二狗子", 90)

std3.print_score_cls()
std4.print_score_cls()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，
# 比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student。
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
#
# 小结
# 数据封装、继承和多态是面向对象的三大特点
