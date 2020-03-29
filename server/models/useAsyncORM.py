#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    这里示例如何使用ORM

"""
# 有了ORM，我们就可以把需要的表（这里是User表）用Model表示出来（继承Model）：
import time, uuid

from  server.models.asyncorm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


"""
------------------------------------------------   一条分割线  ----------------------------------------------------
"""


from server.models import asyncorm

def test():
    loop=asyncio.get_event_loop() 
    yield from asyncorm.create_pool(loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
"""
user=User(id="100001",name="Andy",password="*****")
user.save()  //保存到数据库
user=User.findById("100001") #从数据库中找出id为"100001"的用户
user.update(password="*********")  #更改id为"100001"的用户密码
users=User.findAll() #取出users表中全部数据
"""
#for x in test():
#    pass