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
        print(line.strip())  # 把末尾的'\n'删掉
