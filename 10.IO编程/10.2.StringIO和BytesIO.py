# author:checky

# 在内存中读写数据

# 1、StringIO
from io import StringIO

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
f = StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())
# hello world

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f1 = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f1.readline()
    if s == "":
        break
    print(s.strip())
# Hello!
# Hi!
# Goodbye!

# 2、BytesIO
# 操作二进制数据，就需要使用BytesIO

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f2 = BytesIO()
f2.write("你好".encode("utf-8")) # 写入的不是str，而是经过UTF-8编码的bytes。
print(f2.getvalue())
# b'\xe4\xbd\xa0\xe5\xa5\xbd'

# StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f3 = BytesIO(b"\xe4\xbd\xa0\xe5\xa5\xbd")
print(f3.read())
