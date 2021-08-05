# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from novel.items import bookinfo,bookcontent
import os

charpter_dict = {}

class NovelPipeline:
    def process_item(self, item, spider):
        if isinstance(item,bookinfo):
            bookname = str(item['bookname'])
            if not os.path.exists('{}'.format(bookname)):
                os.mkdir('{}'.format(bookname))
            for charpter in item['charpters']:
                filepath = bookname+'/{}.txt'.format(charpter)
                charpter_dict.update({charpter.strip():filepath})

        elif isinstance(item,bookcontent):
            for key,value in charpter_dict.items():
                if item['title'] == key:
                    with open(value, 'a', encoding='utf-8') as f:
                        f.write('\n'.join(item['content']))
                    f.close()

