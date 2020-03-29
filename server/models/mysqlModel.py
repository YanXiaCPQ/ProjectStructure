#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 只在私有环境用这个类，毕竟不安全，有sql注入风险

from server.logger import sqllog
import pymysql

class MysqlModel(object):
    def __init__(self,**kw):
        self.host = kw.get('host', 'localhost')
        self.user = kw['user']
        self.password = kw['password']
        self.port = kw.get('port', 3306)	
        self.database = kw['db']
        self.charset = kw.get('charset', 'utf8')
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port)

    def update(self, **kwargs):
        sqllog.info('update data')
        cursor = self.conn.cursor()
        args = (kwargs['result'], kwargs['id'])
        sql = """update mc_conbin_testreq_detail set result=%s, where id=%s; """
        self.execute(cursor, sql, args)


    def select(self):
        cursor = self.conn.cursor()
        sqllog.info('selcet from db')
        sql = """select * from xxx ;"""
        try:
            cursor.execute(sql)
            req = cursor.fetchall()
            table_key = cursor.description
            cursor.close()
            self.conn.close()
            return req,table_key
        except:
            self.conn.close()
            sqllog.error("unable to fecth data, please check the sql :" + sql)
            return None, None

    def insert(self):
        cursor = self.conn.cursor()
        sqllog.info('insert to db')
        sql = """insert into tablename (colsName) values(values)"""
        self.execute(cursor, sql)
        
        
    
    def delete(self):
        cursor = self.conn.cursor()
        sqllog.info('delete from db')
        sql = """delete * from xxx ;"""
        self.execute(cursor, sql)
     

    def execute(self, cursor, sql, args=None):
        try:
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            self.conn.commit()
            self.conn.close()            
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            sqllog.errot('delete data error')
            sqllog.error(e)  