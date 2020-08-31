# Coding: utf-8
# Author: Wang Shuai
# Author_Email: wangshuai@ximalayaos.com
# Time: 2020/8/15 0015 16:05
# File: common_mysql.py
# Project_Name: webCrawler
# Content:

import pymysql

'''
#建立连接
get_conn=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='test')
#获取容器：通过建立游标对象：一组sql语句的集合
get_cursor=get_conn.cursor()
#创建表，查数据。。。
str_drop_sql='drop table if exists baga' #if exists 如果存在相同的表明则删除
str_create_sql='create table baga(name varchar(10),price int ,color varchar(20))'
str1='select * from ecs_tag'

#执行sql
get_cursor.execute(str1)
get_cursor.execute(str_drop_sql)
get_cursor.execute(str_create_sql)

#关闭连接
get_conn.close()
print(str1)
'''


class Pymysql:  # host-->本机或ip地址 port-->端口号 database-->数据库名字
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # 连接数据库
    def mysql_connect(self):
        get_conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database
                                   )
        return get_conn

    # 获取游标
    def mysql_cursor(self):
        get_cursor = self.mysql_connect().cursor()
        return get_cursor

    # 创建表
    def mysql_createTable(self, tableName, id, name, author, content, tag):
        self.table1 = tableName
        str_drop_sql = 'drop table if exists {}'.format(self.table1)
        str_create_sql = 'create table {}({} varchar(100),{} varchar(100), {} varchar(100), {} varchar(100), {} varchar(100))'.format(
            tableName, id, name, author, content, tag)
        # print(str_create_sql)

        self.mysql_cursor().execute(str_drop_sql)
        self.mysql_cursor().execute(str_create_sql)

    # 关闭连接
    def mysql_close(self):
        self.mysql_connect().close()

    # 查询
    def mysql_select(self):
        str_select_sql = 'select id from gushici'
        aaa = self.mysql_cursor().execute(str_select_sql)
        print(aaa)

    def mysql_insert(self):
        str_insert_sql = 'insert into gushici (id, name, author, content, tag) values (年后, aad, 拿到, 爱大师, a)'
        self.mysql_cursor().execute(str_insert_sql)



# 创建对象进行调用
if __name__ == '__main__':
    create_table = Pymysql('localhost', 3306, 'root', 'root', 'test')
    create_table.mysql_createTable('gushici', 'id', 'name', 'author', 'content', 'tag')
    create_table.mysql_insert()
    create_table.mysql_select()
    # create_table.mysql_insert(('id', 'name', 'author', 'content', 'tag'),('Bill', 'Xuanwumen', 'Beijing', 'tag', 'a'))
    # create_table.mysql_select()
    create_table.mysql_close()
