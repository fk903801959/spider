# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieListItem(scrapy.Item):
    name = scrapy.Field()

class MovieInfoItem(scrapy.Item):
    movie_name = scrapy.Field()
    tag = scrapy.Field()
