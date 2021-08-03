# -*- coding: utf-8 -*-
# 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。
# 当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyFirstPipeline:
    def process_item(self, item, spider):
        return item
