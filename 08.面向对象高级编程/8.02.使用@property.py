# author:checky
# Python内置的@property装饰器就是负责把一个方法变成属性调用:

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("分数必须为整数")
        if score < 0 or score > 100:
            raise ValueError("分数必须在 0 ~ 100 之内！")
        self._score = score

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, int):
            raise ValueError("出生年份必须为整数！")
        if value < 0:
            raise ValueError("出生年份必须大于0！")
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth


# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

s = Student()
s.score = 99
print(s.score)

s1 = Student()
s1.birth = 1999
print(s1.birth, s1.age)


# s1.age = 21


# AttributeError: can't set attribute

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


class Apple(object):

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("价格必须为数字！")
        if value < 0:
            raise ValueError("价格必须大于0")
        self._price = value


a = Apple()
a.price = 5.6
print(a.price)
