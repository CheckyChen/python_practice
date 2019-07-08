# author:checky

# 1、读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('test.txt', 'r', encoding='utf-8')
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txe'

# 阅读内容
# 避免长时间占用文件资源，可用try...except...finally，在finally中释放资源
print(f.read())

try:
    f2 = open('test.txt', 'r', encoding='utf-8')
    print(f2.read())
except FileNotFoundError:
    print('没有找到文件！')
finally:
    if f2:
        f2.close()


# 每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('test.txt','r',encoding='utf-8') as f:
    print(f.read())


# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
#
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，
# 调用readlines()最方便：

with open('test1.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())  # strip() 把末尾的'\n'删掉


# file like object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
# 还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件：
with open("test.jpg","rb") as f:
    print(f.read())
    # b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x01, # 十六进制表示的字节

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# with open("test.txt",encoding="gbk") as f:
#     print(f.read())


# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# with open("test.txt",encoding='gbk',errors="ignore") as f:
#     print(f.read())


# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

f = open("test2.txt","w")
f.write("写入一行数据\n")
f.close()

# 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
# 而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open("test2.txt","w",encoding="utf-8") as f:
    f.write("第二行数据\n")

# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

# 追加的方式写入文件

with open("test2.txt","a",encoding="utf-8") as f:
    f.write("第三行数据\n")



