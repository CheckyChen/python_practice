# author:checky

# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
#
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
#
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
#
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

import sqlite3


def create_con():
    return sqlite3.connect('test.db')

def create_table():
    con = create_con()
    cursor = con.cursor()
    cursor.execute("create table user (userid int primary key,name varchar(20))")

def insert_data():
    con = create_con()
    cursor = con.cursor()
    # cursor.execute("create table user (userid int primary key,name varchar(20))")
    cursor.execute("insert into user values(0,'checky')")
    rowcount = cursor.rowcount
    print(rowcount)
    cursor.close()
    con.commit()
    con.close()

def search_data():
    con = create_con()
    cursor = con.cursor()
    cursor.execute("select * from user where userid =?",(0,))
    data = cursor.fetchall()
    print(data)
    # [(0, 'checky')]
    user = cursor.fetchone()
    print(user)
    # None
    many = cursor.fetchmany(2)
    print(many)
    # []
    cursor.close()
    con.close()

# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
#
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
#
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
#
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
#
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))


if __name__ == "__main__":
    search_data()

