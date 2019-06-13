# author:checky

# 1、字符编码

# ①ASCII编码：由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122
# ②GB2312编码：中华人民共和国国家标准简体中文字符集，要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去
# ③Unicode编码：Unicode把所有语言都统一到一套编码里，，这样就不会再有乱码问题了

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

# 2、字符串

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

print("hello，我爱中国")

print(ord("A"))     # 获取字符的整数表示,输出：65
print(ord("中"))     # 输出：20013
print(chr(66))      # 把编码转换为对应的字符，输出：B
print(chr(25991))   # 输出：文

# 2.1 将字符转为字节

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

x = b'abc'
print(x)

# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))    # 输出：b'ABC'
print('中文'.encode('utf-8'))    # 输出：b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii'))    # 报错，因为中文编码范围超过了ascii编码的范围，python会报错，can't encode characters in position 0-1: ordinal not in range(128)

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 2.2 将字节转为字符

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'abc'.decode('utf-8'))                      # 输出：adc
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # 输出：中文

# 如果bytes中包含无法解码的字节，decode()方法会报错：
# print(b'\xe4\xb8\xad\xff'.decode('utf-8')) # 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte

# 忽略部分错误的字节 decode()的 errors参数设为 ignors
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors="ignore"))

# 2.3 计算字符的长度len()
print(len("abc"))            # 3
print(len("中华人民共和国"))   # 7

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'abc'))                      # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6
print(len('中国'.encode('utf-8')))       # 6

# 可见：1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

# 3、格式化

# 3.1 打印的格式化

print('你好，我是%s，今年%s岁'%('checky',28))

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))  # %2d 整数占两位，不足两位用空格占位，%02d 占两位，不足，前面补0
print('%.2f' % 3.1415926)   # 保留两位小数

# 字符里面包含 % 怎么办，用转义 %% 就行了
print('占比：%d%%'%50)

# 4 format() 格式化：

a = '这是一个{0}教程，{1}要好好学习，大概花费{2:.2f}学时'
print(a.format('python','小明',12.444))

