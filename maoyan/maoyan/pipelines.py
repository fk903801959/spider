# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymysql import connect

# 使用mongodb数据库存储数据（不需要手动创建数据库和集合，执行命令的同时会自动创建）
class MongoPipeline:
    def open_spider(self,spider):
        self.client = MongoClient()  # 创建连接实例
        self.db = self.client.movie  # 创建数据库实例
        self.collection = self.db.maoyan  # 创建集合实例

    def process_item(self, item, spider):
        self.collection.insert(item)  # 集合实例使用insert方法插入数据，因为item本身即字典格式，故无需做其他处理，可直接插入。
        return item

    def close_spider(self,spider):
        self.client.close() # 关闭数据库连接


# 使用mysql数据库存储数据（需要手动创建数据库和表，执行命令前需提前手动创建）
class MysqlPipeline:
    def open_spider(self, spider):
        self.client = connect(host='localhost',port=3306,user='root',password='root',db='movie',charset='utf8') #创建连接实例，需指明主机地址，端口号，用户名，密码，连接的数据库和编码格式等信息。
        self.cursor = self.client.cursor()  # 创建游标实例

    def process_item(self, item, spider):
        sql = 'insert into maoyan values(0,%s,%s)' # 编写sql语句，用来插入数据（第一列的0表示整型数字且自增，常用作编号主键）
        self.cursor.execute(sql,[item['name'],item['star']]) # 游标实例执行sql语句，将数据以数组的形式传入
        self.client.commit()  # 提交事务
        return item

    def close_spider(self,spider):
        self.cursor.close()  # 关闭游标
        self.client.close()  # 关闭连接
