# author:checky

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

 # 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
#
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 你只需要根据需要替换掉用户名、口令等信息即可。
#
# 下面，我们看看如何向数据库表中添加一行记录。
#
# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Checky')

# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
#
# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：

session = DBSession()
user = session.query(User).filter(User.id == '5').one()

print('type:', type(user))
print('name:', user.name)

session.close()

# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
#
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
#
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：


from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    book = relationship("Book")

class Book(Base):
    __tablename__ = 'book'
    id= Column(String(20),primary_key=True)
    name = Column(String(20))

    user_id = Column(String(20),ForeignKey("user.id"))


# 小结
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
#
# 正确使用ORM的前提是了解关系数据库的原理。
