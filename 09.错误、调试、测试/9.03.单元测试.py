# author:checky

# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
# 比如对函数abs()，我们可以编写出以下几个测试用例：
#   1、输入正数，比如1、1.2、0.99，期待返回值与输入相同；
#   2、输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
#   3、输入0，期待返回0；
#   4、输入非数值类型，比如None、[]、{}，期待抛出TypeError。
# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
# 如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，
# 要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。
# 单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，
# 如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，
# 说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，
# 可以极大程度地保证该模块行为仍然是正确的。

class Dict(dict):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r'该对象不存在该属性：%s' % item)

    def __setattr__(self, key, value):
        self[key] = value


# 写单元测试
import unittest


class TestDict(unittest.TestCase):

    def setUp(self):
        print("setUp....")

    def tearDown(self):
        print("tearDown...")

    def test_init(self):
        d = Dict(a=1, b='test')
        # 断言函数返回的结果与1相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

# 运行单元测试
if __name__ == "__main__":
    unittest.main()

# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
# $ python -m unittest mydict_test

# etUp与tearDown
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
#
# setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，
# 在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：


# 小结
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
