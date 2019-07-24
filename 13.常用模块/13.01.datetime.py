# author:checky

# 1、获取当前时间

from datetime import datetime

now = datetime.now()
print(now,type(now))
# 2019-07-25 06:45:45.182219
# <class 'datetime.datetime'>

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。

# 2、获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：

dt = datetime(2015,4,19,12,20)
print(dt)
# 2015-04-19 12:20:00

# 3、datetime 转化为 timestamp

# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
#
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：

dt = datetime(2019,7,25,6,52)
print(dt.timestamp())
# 1564008720.0

# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
#
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

# 4、timestamp 转换为 datetime

# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：

t = 1564008720.0
print(datetime.fromtimestamp(t))
# 2019-07-25 06:52:00

# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))
# 2019-07-24 22:52:00
# 相差8个小时

# 5、str 转换为 datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

current_day = datetime.strptime('2019-7-25 6:59:22','%Y-%m-%d %H:%M:%S')
print(current_day)
# 2019-07-25 06:59:22
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式,详细链接：https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# 注意转换后的datetime是没有时区信息的。

# 6、datetime 转化为 str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
# 2019-07-25 07:04:54
print(now.strftime('%a, %b %d %H:%M'))
# Thu, Jul 25 07:05

# 7、datetime 加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

from datetime import timedelta
now = datetime.now()
print(now)
# 2019-07-25 07:08:45.731153
print(now + timedelta(hours=10))
# 2019-07-25 17:08:45.731153
print(now + timedelta(days=1))
# 2019-07-26 07:08:45.731153
print(now + timedelta(days=2, hours=12))
# 2019-07-27 19:09:44.731153
