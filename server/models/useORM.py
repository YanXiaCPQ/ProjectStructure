#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    这里示例如何使用ORM

"""
# 有了ORM，我们就可以把需要的表（这里是User表）用Model表示出来（继承Model）：
import time, uuid

from  server.models.orm import Model, StringField, BooleanField, FloatField, TextField

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
#  编写数据访问代码

from server.models import orm 
def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

#for x in test():
#    pass