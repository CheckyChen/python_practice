from enum import Enum

Month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, member.value)
    # value属性则是自动赋给成员的int常量，默认从1开始计数。

    # Jan => Month.Jan 1
    # Feb => Month.Feb 2
    # Mar => Month.Mar 3
    # Apr => Month.Apr 4
    # May => Month.May 5
    # Jun => Month.Jun 6
    # Jul => Month.Jul 7
    # Aug => Month.Aug 8
    # Sep => Month.Sep 9
    # Oct => Month.Oct 10
    # Nov => Month.Nov 11
    # Dec => Month.Dec 12

for name, member in Month.__members__.items():
    print(name, member, member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum,unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 访问枚举类型的方法
d1 = Weekday.Sun
print(d1)
# Weekday.Sun

d2 = Weekday['Sat']
print(d2)
# Weekday.Sat

print(Weekday['Sat'].value)
# 6

print(Weekday(1))
# Weekday.Mon

print(d1 == Weekday(0))
# True
