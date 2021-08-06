# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class bookinfo(scrapy.Item):
    bookname = scrapy.Field()
    charpters = scrapy.Field()

class bookcontent(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class bookcontent2(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
