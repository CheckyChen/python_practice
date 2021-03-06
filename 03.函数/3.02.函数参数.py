# author:checky

# 1、位置参数
def power(x):
    return x ** 2


print(power(2))


# 2、默认参数
def power(a, n=2):
    x = 1
    i = 1
    while i <= n:
        x = x * a
        i = i + 1
    return x


print(power(2, 4))


def add_end(l=[]):
    l.append("end")
    return l


print(add_end([1, 2, 3, 4, 5]))
print(add_end([1, 2, 3, 4, 5]))

print(add_end())  # ['end']
print(add_end())  # ['end', 'end']
print(add_end())  # ['end', 'end', 'end']


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象
# 更正上述问题如下：
def add_end1(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(add_end1())  # ['end']
print(add_end1())  # ['end']
print(add_end1())  # ['end']


# 3、可变参数
def calc(*numbers):
    print(numbers)  # 是一个元组类型
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))

numbers = [1, 2, 3]
print(calc(*numbers))


# 4、关键字参数
# 关键字参数允许你传入0个或任意个包含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('checky', 27)
person('checky', 27, hobby='guitar', gender='男')

extract = {'hobby': 'guitar,basketball', 'gender': '男'}
person('checky', 27, **extract)


# 注意：kw获得的dict是extract的一份拷贝，对kw的改动不会影响到函数外的extract。

# 5、命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，就需要在函数内部通过kw检查
def person1(name, age, **kwargs):
    if 'city' in kwargs:
        # 说明有city参数
        pass
    if 'job' in kwargs:
        # 说明有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kwargs)


# 调用任然可以传入不受限制的关键字参数
person1("Jack", 24, city='beijing', hobby='pingpang')


# 如果要限制关键字参数的名字，就可以用命名关键字参数
def person2(name, age, *, city, zip):
    print(name, age, city, zip)


# person2('张三', 24, hobby='guitar', city=123, zip=456)
# TypeError: person2() got an unexpected keyword argument 'hobby'

person2('张三', 24, city=123, zip=456)


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, zip):
    print(name, age, args, city, zip)


person3('chenzongyan', 27, 1, 2, 3, city='beijing', zip=100000)


# chenzongyan 27 (1, 2, 3) beijing 100000

# 6、组合参数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=123, *args, **kwargs):
    print('a=', a, 'b=', b, 'c=', c, args, kwargs)


def f2(a, b, c=0, *, d, **kwargs):
    print(a, b, c, d, kwargs)


f1(1, 2, 3, 4, 5, hobby='basketball', city='beijing')
f1(1, 2, 5, hobby='basketball', city='beijing')
f1(1, 2, args=1, hobby='basketball', city='beijing')
f2(1, 2, d='3', hobby='basketball', city='beijing')

args = (1, 2, 3, 4)
kw = {'city': 'beijing', 'zip': 100000}
f1(*args, **kw)

# ************所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。*********
