#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: Lang

# 连表操作
# 一对多, 主动指定外键约束

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://chenliang:123456@172.16.131.129:3306/chenliang", max_overflow=5)

Base = declarative_base()


# 单表
class Test(Base):
    __tablename__ = 'test'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))


# 一对多
class Server(Base):
    __tablename__ = 'group'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32))


class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    group_id = Column(Integer, ForeignKey('group.nid'))
    # 与生成表结构无关，仅用于查询方便
    group = relationship("Server", backref='uuu')

    def __repr__(self):
        temp = "%s - %s: %s" % (self.nid, self.username, self.group_id)
        return temp


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()
init_db()

Session = sessionmaker(bind=engine)
session = Session()

session.add(Server(caption='dba'))
session.add(Server(caption='ddd'))
# session.commit()

session.add_all([
    User(username='alex1', group_id=1),
    User(username='alex2', group_id=2)
])
session.commit()

# 只是获取用户
ret = session.query(User).filter(User.username == 'alex1').all()
print(ret)
ret = session.query(User).all()
obj = ret[0]
print(ret)
print(obj)
print(obj.nid)
print(obj.username)
print(obj.group_id)

ret = session.query(User.username).all()
print(ret)
# 获取对象
sql = session.query(User, Server).join(Server, isouter=True)
print(sql)
ret = session.query(User, Server).join(Server, isouter=True).all()
print(ret)

# 获取列表+元祖
sql = session.query(User.username, Server.caption).join(Server, isouter=True)
print(sql)
ret = session.query(User.username, Server.caption).join(Server, isouter=True).all()
print(ret)

# select * from user left join group on user.group_id = group.nid

# relationship和foreignkey一起, 新方式(正向查询)
ret = session.query(User).all()
for obj in ret:
    # obj代指user表的每一行数据
    # obj.group代指group对象
    print(obj.nid, obj.username, obj.group_id, obj.group, obj.group.nid, obj.group.caption)

# 原始方式
ret = session.query(User.username, Server.caption).join(Server, isouter=True).filter(Server.caption == 'DBA').all()
print(ret)

# 新方式(反向查询)
obj = session.query(Server).filter(Server.caption == 'DBA').first()
print(obj.nid)
print(obj.caption)
print(obj.uuu)  # 获取组内的所有人


# 多对多
"""
主机:
1   c1
2   c2
3   c3

服务器用户:
1   root
2   nb
3   db

; 多台服务器共同存在root账号
; 一台服务器可以多个账号登录
关系表:
主机ID    服务器用户ID
  1         1
  1         2
  3         1

# 对于下面这种数据, 需要增加外键约束
  10        5

"""


# 表创建


class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))

    # (Table对象)    host_user = relationship('HostUser', secondary=HostToHostUser, backref='h')
    # host_user = relationship('HostUser', secondary=lambda: HostToHostUser.__table__, backref='h')
    # __table__
    host_user = relationship('HostUser', secondary=lambda: HostToHostUser.__table__, backref='h')


class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))


class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True, autoincrement=True)

    host_id = Column(Integer, ForeignKey('host.nid'))
    host_user_id = Column(Integer, ForeignKey('host_user.nid'))

    # 新式方法relationship
    # host = relationship('Host', backref='h')
    # host_user = relationship('HostUser', backref='u')


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()
# init_db()
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Host(hostname='c1', port='22', ip='1.1.1.1'),
    Host(hostname='c2', port='22', ip='1.1.1.2'),
    Host(hostname='c3', port='22', ip='1.1.1.3'),
    Host(hostname='c4', port='22', ip='1.1.1.4'),
    Host(hostname='c5', port='22', ip='1.1.1.5'),
])
# session.commit()


session.add_all([
    HostUser(username='root'),
    HostUser(username='db'),
    HostUser(username='nb'),
    HostUser(username='sb'),
])
# session.commit()

session.add_all([
    HostToHostUser(host_id=1, host_user_id=1),
    HostToHostUser(host_id=1, host_user_id=2),
    HostToHostUser(host_id=1, host_user_id=3),
    HostToHostUser(host_id=2, host_user_id=2),
    HostToHostUser(host_id=2, host_user_id=4),
    HostToHostUser(host_id=2, host_user_id=3),
])
session.commit()

需求
获取主机1中所有用户

A方式
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# host_obj.nid
host_hostuser = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()

print(host_hostuser)
# [(1,), (2,), (3,)]
r = zip(*host_hostuser)
# print(list(r)[0])
# [1, 2, 3]

users = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
print(users)


原始方式
ret = session.query(HostUser.name).filter(HostUser.nid.in_(session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == session.query(Host.nid).filter(Host.hostname == 'c1'))))

# B方式
"""
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
print(host_obj.nid)
print(host_obj.hostname)
# 获取第三张表对应的对象
print(host_obj.h)

# 循环第三张表对象
for item in host_obj.h:
    print(item.host_user, item.host_user.nid, item.host_user.username)
"""

# C方式
# 精简:
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
for item in host_obj.h:
    print(item.host_user.username)


# 通过这种方式, 只能通过Table对象来操作, 或者通过lamba来实现
"""
UserProfile2Group = Table('userprofile_2_group',Base.metadata,
    Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
    Column('group_id',ForeignKey('group.id'),primary_key=True),
)
"""
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
for item in host_obj.host_user:
    print(item.username)
