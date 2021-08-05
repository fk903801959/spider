# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from yinfansi.items import MovieListItem,MovieInfoItem
from json import dumps

class YinfansiPipeline:
    def open_spider(self,spider):
        self.filename1 = open('movie_list.txt','w',encoding='utf-8')
        self.filename2 = open('movie_info.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item,MovieListItem):
            self.filename1.write(dumps(dict(item),ensure_ascii=False)+'\n')
            return item
        elif isinstance(item,MovieInfoItem):
            self.filename2.write(dumps(dict(item),ensure_ascii=False)+'\n')
            return item
        else:
            return None

    def close_spider(self,spider):
        self.filename1.close()
        self.filename2.close()

