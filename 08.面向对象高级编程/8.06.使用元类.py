# author:checky

# type()函数
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self, name='World'):
    print("Hello,", name)


def test(self):
    print('test function')


# 创建Hello class
Hello = type("Hello", (object,), dict(hello=fn, test=test))
h = Hello()
h.hello()
# Hello, World

h.test()


# test function

# 要创建一个class对象，type()函数依次传入3个参数：
#   1、class的名称；
#   2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#   3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# metaclass

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# 利用元类给我们自定义的MyList添加一个add()方法
# metaclass 是类的模板，所以必须继承 type 类型
class ListMetaclass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, base, attrs)


# 定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
#   1.当前准备创建的类的对象；
#   2.类的名字；
#   3.类继承的父类集合；
#   4.类的方法集合。

l = MyList()
l.add(1)
l.add(1)
l.add(1)
print(l)


# [1, 1, 1]

# 利用metaclass编写一个ORM框架

# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 编写最复杂的ModelMetaclass
class ModelMetaclass(type):

    def __new__(cls, name, base, attrs):
        if name == 'Model':
            return type.__new__(cls, name, base, attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping:%s ==> %s" % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, base, attrs)


# 基于metaclass的基类Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print("SQL:", sql)
        print("ARGS:", args)


# 定义一个User类
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

# Found model:User
# Found mapping:id ==> <IntegerField:id>
# Found mapping:name ==> <StringField:username>
# Found mapping:email ==> <StringField:email>
# Found mapping:password ==> <StringField:password>
# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
