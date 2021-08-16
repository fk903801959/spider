# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class RoomPipeline:
    def open_spider(self,spider):
        self.client = MongoClient()
        self.lianjia = self.client.room.lianjia

    def process_item(self, item, spider):
        self.lianjia.insert(dict(item))
        return item

    def close_item(self,spider):
        self.client.close()
